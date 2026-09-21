# ──────────────────────────────────────────────────
# Problem  : 558. Logical OR of Two Binary Grids Represented as Quad-Trees
# Difficulty: Medium
# Tags     : Divide and Conquer, Tree
# Link     : https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
# Runtime  : 58 ms (beats 66%)
# Memory   : 19816000 (beats 18%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        # If either of the trees is a leaf node, return the appropriate tree
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        
        # Recursively check the intersection of each child node
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # If all four child nodes are leaves with the same value, return a new leaf node
        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
            return Node(tl.val, True, None, None, None, None)
        
        # Otherwise, return a new internal node with the four child nodes as children
        return Node(None, False, tl, tr, bl, br)