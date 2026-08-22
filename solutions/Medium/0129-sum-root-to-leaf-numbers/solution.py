# ──────────────────────────────────────────────────
# Problem  : 129. Sum Root to Leaf Numbers
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19204000 (beats 72%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def sumNumbers(self, root):
        return self.sum(root, 0)

    def sum(self, root, currSum):
        if root is None:
            return 0

        currSum = currSum * 10 + root.val

        if root.left is None and root.right is None:
            return currSum

        return self.sum(root.left, currSum) + self.sum(root.right, currSum)