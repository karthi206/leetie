# ──────────────────────────────────────────────────
# Problem  : 230. Kth Smallest Element in a BST
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Link     : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Runtime  : 0 ms (beats 100%)
# Memory   : 22116000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = 0

        def helper(root):
            if root is None:
                return

            helper(root.left)

            self.count += 1

            if self.count == k:
                self.ans = root.val
                return

            if self.count < k:
                helper(root.right)

        helper(root)

        return self.ans