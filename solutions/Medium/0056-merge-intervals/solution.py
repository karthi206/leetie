# ──────────────────────────────────────────────────
# Problem  : 56. Merge Intervals
# Difficulty: Medium
# Tags     : Array, Sorting, Quicksort
# Link     : https://leetcode.com/problems/merge-intervals/
# Runtime  : 8 ms (beats 44%)
# Memory   : 22820000 (beats 43%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged=[]
        merged.append(intervals[0])
        for current in intervals[1:]:
            last_merged=merged[-1]
            if current[0]<=last_merged[1]:
                last_merged[1]=max(current[1],last_merged[1])
            else:
                merged.append(current)
        return merged