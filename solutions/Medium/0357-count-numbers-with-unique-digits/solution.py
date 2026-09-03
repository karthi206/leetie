# ──────────────────────────────────────────────────
# Problem  : 357. Count Numbers with Unique Digits
# Difficulty: Medium
# Tags     : Math, Dynamic Programming, Backtracking
# Link     : https://leetcode.com/problems/count-numbers-with-unique-digits/
# Runtime  : 706 ms (beats 9%)
# Memory   : 19228000 (beats 56%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    """Pure Backtracking Solution"""

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        def backtrack(length, visited: list):
            if length == n:
                return 0

            count = 0
            for i in range(10):
                if i == 0 and len(visited) == 0:
                    continue
                if i not in visited:
                    visited.append(i)
                    count += 1
                    count += backtrack(length + 1, visited)
                    visited.pop()
            return count

        return 1 + backtrack(0, [])