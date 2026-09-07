# ──────────────────────────────────────────────────
# Problem  : 452. Minimum Number of Arrows to Burst Balloons
# Difficulty: Medium
# Tags     : Array, Greedy, Sorting
# Link     : https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Runtime  : 86 ms (beats 46%)
# Memory   : 53388000 (beats 91%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrows = 1
        end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > end: 
                arrows += 1  
                end = balloon[1] 
            else:
                end = min(end, balloon[1])
        
        return arrows