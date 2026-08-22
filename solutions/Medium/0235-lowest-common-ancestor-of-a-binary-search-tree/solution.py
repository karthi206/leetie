# ──────────────────────────────────────────────────
# Problem  : 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor
# Link     : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Runtime  : 40 ms (beats 0%)
# Memory   : 19112000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root