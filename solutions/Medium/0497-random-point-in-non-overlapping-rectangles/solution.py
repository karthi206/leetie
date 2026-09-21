# ──────────────────────────────────────────────────
# Problem  : 497. Random Point in Non-overlapping Rectangles
# Difficulty: Medium
# Tags     : Array, Math, Binary Search, Reservoir Sampling, Prefix Sum, Ordered Set, Randomized
# Link     : https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19492000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def __init__(self, r: List[List[int]]):
        self.r,self.p = r,[*accumulate((x-a+1)*(y-b+1) for a,b,x,y in r)]

    def pick(self) -> List[int]:
        a,b,x,y = self.r[bisect_left(self.p,randint(1,self.p[-1]))]
        return randint(a,x),randint(b,y)