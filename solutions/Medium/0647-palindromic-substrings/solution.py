# ──────────────────────────────────────────────────
# Problem  : 647. Palindromic Substrings
# Difficulty: Medium
# Tags     : Two Pointers, String, Dynamic Programming
# Link     : https://leetcode.com/problems/palindromic-substrings/
# Runtime  : 124 ms (beats 55%)
# Memory   : 19356000 (beats 39%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def expand(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            return res
            
        for i in range(len(s)):
            count += expand(i, i)     # Odd
            count += expand(i, i + 1) # Even
            
        return count