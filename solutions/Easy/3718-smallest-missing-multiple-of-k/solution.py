# ──────────────────────────────────────────────────
# Problem  : 3718. Smallest Missing Multiple of K
# Difficulty: Easy
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19252000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = [False] * 101

        for num in nums:
            present[num] = True

        multiple = k
        while True:
            if multiple > 100 or not present[multiple]:
                return multiple
            multiple += k