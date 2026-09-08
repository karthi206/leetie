# ──────────────────────────────────────────────────
# Problem  : 508. Most Frequent Subtree Sum
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Binary Tree, DP on Trees
# Link     : https://leetcode.com/problems/most-frequent-subtree-sum/
# Runtime  : 7 ms (beats 19%)
# Memory   : 21544000 (beats 41%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        freq = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            total = node.val + left + right
            freq[total] += 1

            return total

        dfs(root)

        max_freq = max(freq.values())

        return [s for s in freq if freq[s] == max_freq]
        