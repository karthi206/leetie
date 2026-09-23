# ──────────────────────────────────────────────────
# Problem  : 633. Sum of Square Numbers
# Difficulty: Medium
# Tags     : Math, Two Pointers, Binary Search
# Link     : https://leetcode.com/problems/sum-of-square-numbers/
# Runtime  : 74 ms (beats 37%)
# Memory   : 19452000 (beats 28%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):  # Iterate through all possible values of `a`
            b = sqrt(c - a * a)  # Compute `b` as the square root of `c - a^2`
            if b == int(b):  # Check if `b` is an integer
                return True  # If `b` is an integer, return true
        return False  # If no such pair `(a, b)` is found, return false