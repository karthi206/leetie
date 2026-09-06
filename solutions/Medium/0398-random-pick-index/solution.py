# ──────────────────────────────────────────────────
# Problem  : 398. Random Pick Index
# Difficulty: Medium
# Tags     : Hash Table, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/random-pick-index/
# Runtime  : 46 ms (beats 32%)
# Memory   : 29652000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:

    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])