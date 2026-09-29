# ──────────────────────────────────────────────────
# Problem  : 654. Maximum Binary Tree
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree, Cartesian Tree
# Link     : https://leetcode.com/problems/maximum-binary-tree/
# Runtime  : 7 ms (beats 98%)
# Memory   : 19668000 (beats 41%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nodes = []
        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()

            if nodes:
                nodes[-1].right = node

            nodes.append(node)

        return nodes[0]