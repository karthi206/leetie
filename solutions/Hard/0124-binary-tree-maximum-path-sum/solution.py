# ──────────────────────────────────────────────────
# Problem  : 124. Binary Tree Maximum Path Sum
# Difficulty: Hard
# Tags     : Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Runtime  : 14 ms (beats 17%)
# Memory   : 23836000 (beats 63%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.ans