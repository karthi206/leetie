# ──────────────────────────────────────────────────
# Problem  : 836. Rectangle Overlap
# Difficulty: Easy
# Tags     : Math, Geometry
# Link     : https://leetcode.com/problems/rectangle-overlap/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19428000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        return not (
            rec1[2] <= rec2[0] or  # rec1 is left of rec2
            rec1[0] >= rec2[2] or  # rec1 is right of rec2
            rec1[3] <= rec2[1] or  # rec1 is below rec2
            rec1[1] >= rec2[3]     # rec1 is above rec2
        )