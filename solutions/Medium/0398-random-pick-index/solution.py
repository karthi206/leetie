# ──────────────────────────────────────────────────
# Problem  : 398. Random Pick Index
# Difficulty: Medium
# Tags     : Hash Table, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/random-pick-index/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19420000 (beats 0%)
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