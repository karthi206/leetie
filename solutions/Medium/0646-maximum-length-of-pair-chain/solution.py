# ──────────────────────────────────────────────────
# Problem  : 646. Maximum Length of Pair Chain
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy, Sorting, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/maximum-length-of-pair-chain/
# Runtime  : 11 ms (beats 47%)
# Memory   : 19632000 (beats 34%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findLongestChain(self, pairs):

        pairs.sort(key=lambda x: x[1])

        end = pairs[0][1]
        chain = 1

        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                chain += 1
                end = pairs[i][1]

        return chain