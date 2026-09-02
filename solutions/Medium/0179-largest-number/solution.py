# ──────────────────────────────────────────────────
# Problem  : 179. Largest Number
# Difficulty: Medium
# Tags     : Array, String, Greedy, Sorting
# Link     : https://leetcode.com/problems/largest-number/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19188000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from typing import List
        from functools import cmp_to_key
        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        strs=list(map(str,nums))
        strs.sort(key=cmp_to_key(compare))
        result=''.join(strs)
        return '0' if result[0] == '0' else result