# ──────────────────────────────────────────────────
# Problem  : 313. Super Ugly Number
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming
# Link     : https://leetcode.com/problems/super-ugly-number/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19320000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        k = len(primes)

        ptr = [0] * k
        next = list(primes)

        for i in range(1, n):
            next_ugly = min(next)
            ugly[i] = next_ugly

            for j in range(k):
                if next[j] == next_ugly:
                    ptr[j] += 1
                    next[j] = primes[j] * ugly[ptr[j]]
        return ugly[n - 1]