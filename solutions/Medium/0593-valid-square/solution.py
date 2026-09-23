# ──────────────────────────────────────────────────
# Problem  : 593. Valid Square
# Difficulty: Medium
# Tags     : Math, Geometry
# Link     : https://leetcode.com/problems/valid-square/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19304000 (beats 45%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1,point2):
            return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2
            
        D=[
        dist(p1,p2),
        dist(p1,p3),
        dist(p1,p4),
        dist(p2,p3),
        dist(p2,p4),
        dist(p3,p4)
        ]
        D.sort()
        return 0<D[0]==D[1]==D[2]==D[3] and D[4]==D[5]
        