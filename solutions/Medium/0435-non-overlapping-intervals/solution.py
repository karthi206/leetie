# ──────────────────────────────────────────────────
# Problem  : 435. Non-overlapping Intervals
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy, Sorting
# Link     : https://leetcode.com/problems/non-overlapping-intervals/
# Runtime  : 76 ms (beats 63%)
# Memory   : 49076000 (beats 56%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]
        
        return res