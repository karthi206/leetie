# ──────────────────────────────────────────────────
# Problem  : 437. Path Sum III
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/path-sum-iii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19312000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:

    def pathSum(self, root, targetSum):

        self.ans = 0

        # Counts all valid paths starting from the current node.
        def dfs(node, cur):

            if not node:
                return

            cur += node.val

            if cur == targetSum:
                self.ans += 1

            dfs(node.left, cur)
            dfs(node.right, cur)

        if not root:
            return 0

        stack = [root]

        # Every node becomes a starting point.
        while stack:

            node = stack.pop()

            dfs(node, 0)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return self.ans