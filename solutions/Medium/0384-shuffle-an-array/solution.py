# ──────────────────────────────────────────────────
# Problem  : 384. Shuffle an Array
# Difficulty: Medium
# Tags     : Array, Math, Design, Randomized
# Link     : https://leetcode.com/problems/shuffle-an-array/
# Runtime  : 11 ms (beats 96%)
# Memory   : 22708000 (beats 26%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from random import randint


class Solution:
    def __init__(self, nums: List[int]):
        self.duplicate = nums[:]
        self.nums = nums
        self.l = len(nums)

        
    def reset(self) -> List[int]:
        self.nums[:] = self.duplicate
        return self.nums

    
    def shuffle(self) -> List[int]:
        arr = self.nums
        
        
        for i in range(self.l):
            j = randint(i, self.l - 1)
            arr[i], arr[j] = arr[j], arr[i]
        
        
        return arr