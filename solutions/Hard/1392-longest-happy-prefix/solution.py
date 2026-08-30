# ──────────────────────────────────────────────────
# Problem  : 1392. Longest Happy Prefix
# Difficulty: Hard
# Tags     : String, Rolling Hash, String Matching, Hash Function, Z Algorithm, Knuth–Morris–Pratt Algorithm
# Link     : https://leetcode.com/problems/longest-happy-prefix/
# Runtime  : 87 ms (beats 76%)
# Memory   : 24076000 (beats 61%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def longestPrefix(self, s: str) -> str:
        n=len(s)
        lps=[0]*n
        lene=0
        i=1
        while i<n:
            if s[i] == s[lene]:
                lene+=1
                lps[i]=lene
                i+=1
            else:
                if lene>0:
                    lene=lps[lene-1]
                else:
                    lps[i]=0
                    i+=1
        return s[:lps[-1]]
