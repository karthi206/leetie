# ──────────────────────────────────────────────────
# Problem  : 233. Number of Digit One
# Difficulty: Hard
# Tags     : Math, Dynamic Programming, Recursion
# Link     : https://leetcode.com/problems/number-of-digit-one/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19236000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        p = 1  # position (units, tens, hundreds...)
        while p <= n:
            higher = n // (p * 10)
            current = (n // p) % 10
            lower = n % p

            if current == 0:
                count += higher * p
            elif current == 1:
                count += higher * p + lower + 1
            else:
                count += (higher + 1) * p

            p *= 10
        return count