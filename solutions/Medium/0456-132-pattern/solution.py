# ──────────────────────────────────────────────────
# Problem  : 456. 132 Pattern
# Difficulty: Medium
# Tags     : Array, Binary Search, Stack, Monotonic Stack, Ordered Set
# Link     : https://leetcode.com/problems/132-pattern/
# Runtime  : 43 ms (beats 79%)
# Memory   : 36544000 (beats 20%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, third = [], float('-inf')
        
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        return False