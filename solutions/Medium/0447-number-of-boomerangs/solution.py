# ──────────────────────────────────────────────────
# Problem  : 447. Number of Boomerangs
# Difficulty: Medium
# Tags     : Array, Hash Table, Math
# Link     : https://leetcode.com/problems/number-of-boomerangs/
# Runtime  : 263 ms (beats 99%)
# Memory   : 19344000 (beats 72%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numberOfBoomerangs(self, points):
        n = 0
        for a,b in points:
            counter = {}
            for x,y in points:
                # NOTE: x,y == a,b can only be registered once, so...
				#       radius=0 never has enough points to make a false triplet
                key = (x-a)**2 + (y-b)**2
                if key in counter:
                    n += 2*counter[key]
                    counter[key] += 1
                else:
                    counter[key] = 1
        return n