# ──────────────────────────────────────────────────
# Problem  : 201. Bitwise AND of Numbers Range
# Difficulty: Medium
# Tags     : Bit Manipulation
# Link     : https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19252000 (beats 52%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt