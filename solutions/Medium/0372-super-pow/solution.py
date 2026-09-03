# ──────────────────────────────────────────────────
# Problem  : 372. Super Pow
# Difficulty: Medium
# Tags     : Math, Divide and Conquer, Euler's Totient Function, Euler's Theorem
# Link     : https://leetcode.com/problems/super-pow/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19500000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    MOD = 1337

    def pow(self, a: int, b: int) -> int:
        result = 1
        a %= self.MOD  # Taking mod to prevent overflow
        for _ in range(b):
            result = (result * a) % self.MOD
        return result

    def superPow(self, a: int, b: list[int]) -> int:
        result = 1
        for i in range(len(b) - 1, -1, -1):
            result = (result * self.pow(a, b[i])) % self.MOD
            a = self.pow(a, 10)  # Power up for the next iteration
        return result