# ──────────────────────────────────────────────────
# Problem  : 538. Convert BST to Greater Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/convert-bst-to-greater-tree/
# Runtime  : 7 ms (beats 15%)
# Memory   : 21168000 (beats 63%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def __init__(self):
        self.curr = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.right = self.convertBST(root.right)
        self.curr += root.val
        root.val = self.curr
        root.left = self.convertBST(root.left)
        return root