# ──────────────────────────────────────────────────
# Problem  : 1668. Maximum Repeating Substring
# Difficulty: Easy
# Tags     : String, Dynamic Programming, String Matching
# Link     : https://leetcode.com/problems/maximum-repeating-substring/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19200000 (beats 87%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=1
        while (word*k)in sequence:
            k+=1
        return k-1