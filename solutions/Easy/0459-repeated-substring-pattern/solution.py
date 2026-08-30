# ──────────────────────────────────────────────────
# Problem  : 459. Repeated Substring Pattern
# Difficulty: Easy
# Tags     : String, String Matching, Z Algorithm, Knuth–Morris–Pratt Algorithm
# Link     : https://leetcode.com/problems/repeated-substring-pattern/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19300000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
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
        chunk=n-lps[-1]
        if lps[-1]!= 0 and n%chunk ==0 :
            res=True
        else:
            res=False
        return res