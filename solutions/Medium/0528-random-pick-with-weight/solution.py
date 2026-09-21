# ──────────────────────────────────────────────────
# Problem  : 528. Random Pick with Weight
# Difficulty: Medium
# Tags     : Array, Math, Binary Search, Prefix Sum, Randomized
# Link     : https://leetcode.com/problems/random-pick-with-weight/
# Runtime  : 29 ms (beats 98%)
# Memory   : 24356000 (beats 90%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.prefix_sums, target)