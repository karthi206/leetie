# ──────────────────────────────────────────────────
# Problem  : 264. Ugly Number II
# Difficulty: Medium
# Tags     : Hash Table, Math, Dynamic Programming, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/ugly-number-ii/
# Runtime  : 83 ms (beats 22%)
# Memory   : 19580000 (beats 12%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2,3,5]
        uglyHeap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            curr = heappop(uglyHeap)
            for prime in primes:
                new_ugly = curr * prime
                if new_ugly not in visited:
                    heappush(uglyHeap, new_ugly)
                    visited.add(new_ugly)
        return curr