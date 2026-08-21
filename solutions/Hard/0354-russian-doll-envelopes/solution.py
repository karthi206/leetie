# ──────────────────────────────────────────────────
# Problem  : 354. Russian Doll Envelopes
# Difficulty: Hard
# Tags     : Array, Binary Search, Dynamic Programming, Sorting, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/russian-doll-envelopes/
# Runtime  : 125 ms (beats 60%)
# Memory   : 54992000 (beats 39%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))        
        res = []
        for _, h in envelopes:
            idx = bisect_left(res, h)
            if idx == len(res):
                res.append(h)
            else:
                res[idx]=h
        return len(res)                                                                                              