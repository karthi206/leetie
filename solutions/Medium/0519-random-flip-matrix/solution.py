# ──────────────────────────────────────────────────
# Problem  : 519. Random Flip Matrix
# Difficulty: Medium
# Tags     : Hash Table, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/random-flip-matrix/
# Runtime  : 19 ms (beats 5%)
# Memory   : 19884000 (beats 21%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from sortedcontainers import SortedSet

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.oneIdxs = SortedSet()

    def flip(self) -> List[int]:
        remainingZeros = self.m * self.n - len(self.oneIdxs)
        zeroIdx = randint(0, remainingZeros - 1)

        idx = zeroIdx
        ones_before_idx = self.oneIdxs.bisect_right(idx) # O(log Flips)
        while idx != zeroIdx + ones_before_idx: # ~O(log Flips) loops
            idx = zeroIdx + ones_before_idx
            ones_before_idx = self.oneIdxs.bisect_right(idx) # O(log Flips)
        
        self.oneIdxs.add(idx)

        return [idx // self.n, idx % self.n]
        
    def reset(self) -> None:
        self.oneIdxs = SortedSet()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()