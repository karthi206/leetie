# ──────────────────────────────────────────────────
# Problem  : 400. Nth Digit
# Difficulty: Medium
# Tags     : Math, Binary Search
# Link     : https://leetcode.com/problems/nth-digit/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19172000 (beats 87%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def findNthDigit(self, n):
        i = 1
        count = 9
        start = 1

        while n > i * count:
            n -= i * count
            i += 1
            count *= 10
            start *= 10

        number = start + (n - 1) // i
        return int(str(number)[(n - 1) % i])