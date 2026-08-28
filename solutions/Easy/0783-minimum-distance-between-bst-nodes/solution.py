# ──────────────────────────────────────────────────
# Problem  : 783. Minimum Distance Between BST Nodes
# Difficulty: Easy
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19428000 (beats 10%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = float('inf')
        self.pred = None
        self.inorder(root)
        return self.ans

    def inorder(self, root: TreeNode) -> None:
        if root is None:
            return
        
        self.inorder(root.left)
        if self.pred is not None:
            self.ans = min(self.ans, root.val - self.pred)
        self.pred = root.val
        self.inorder(root.right)