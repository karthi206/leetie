# ──────────────────────────────────────────────────
# Problem  : 3483. Unique 3-Digit Even Numbers
# Difficulty: Easy
# Tags     : Array, Hash Table, Recursion, Enumeration
# Link     : https://leetcode.com/problems/unique-3-digit-even-numbers/
# Runtime  : 79 ms (beats 20%)
# Memory   : 19468000 (beats 20%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        f = Counter(digits)

        res = 0
        for n in range(100, 1000, 2):
            i, rem = divmod(n, 100)
            j, k = divmod(rem, 10)
            res += f[i] > 0 and f[j] > (i == j) and f[k] > (i == k) + (j == k)

        return res