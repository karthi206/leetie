# ──────────────────────────────────────────────────
# Problem  : 3414. Maximum Score of Non-overlapping Intervals
# Difficulty: Hard
# Tags     : Array, Binary Search, Dynamic Programming, Sorting
# Link     : https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
# Runtime  : 1445 ms (beats 69%)
# Memory   : 51996000 (beats 99%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][1])  # by right endpoint
        rights = [intervals[i][1] for i in order]

        prev = [(0, ())] * (n + 1)  # k = 0: nothing picked
        for _ in range(4):
            cur = [(0, ())] * (n + 1)
            for p in range(1, n + 1):
                i = order[p - 1]  # take next interval
                l, r, w = intervals[i]
                j = bisect_left(rights, l)  # intervals ending before l
                score, ids = prev[j]
                cur[p] = min((score - w, tuple(sorted(ids + (i,)))), cur[p - 1])
            prev = cur

        return list(prev[n][1])