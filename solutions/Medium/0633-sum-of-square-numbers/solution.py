# ──────────────────────────────────────────────────
# Problem  : 633. Sum of Square Numbers
# Difficulty: Medium
# Tags     : Math, Two Pointers, Binary Search
# Link     : https://leetcode.com/problems/sum-of-square-numbers/
# Runtime  : 69 ms (beats 40%)
# Memory   : 19208000 (beats 88%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c)) + 1):  
            b = sqrt(c - a * a)  
            if b == int(b):  
                return True  
        return False  