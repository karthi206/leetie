# ──────────────────────────────────────────────────
# Problem  : 806. Number of Lines To Write String
# Difficulty: Easy
# Tags     : Array, String
# Link     : https://leetcode.com/problems/number-of-lines-to-write-string/
# Runtime  : 69 ms (beats 0%)
# Memory   : 19256000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        total = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if total + w > 100:
                lines += 1
                total = 0
            total += w
        return [lines, total]