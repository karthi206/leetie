# ──────────────────────────────────────────────────
# Problem  : 223. Rectangle Area
# Difficulty: Medium
# Tags     : Math, Geometry
# Link     : https://leetcode.com/problems/rectangle-area/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19256000 (beats 89%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) -> int:
        
        int_area = (max((min(ay2, by2)-max(ay1, by1)),0)*               #  int_area is the area of the rectangles' 
                    max((min(ax2, bx2)-max(ax1, bx1)),0))               #  intersection. If no intersection, int_area == 0
                       
        return ((ax2-ax1)*(ay2-ay1) +                                   #  area of rectangle A +
                (bx2-bx1)*(by2-by1) -                                   #  area of rectangle B -
                int_area              )                                 #  area of the intersection, if any