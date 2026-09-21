# ──────────────────────────────────────────────────
# Problem  : 522. Longest Uncommon Subsequence II
# Difficulty: Medium
# Tags     : Array, Hash Table, Two Pointers, String, Sorting
# Link     : https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Runtime  : 93 ms (beats 13%)
# Memory   : 31496000 (beats 8%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        d=defaultdict(lambda:0)
        def trv(word,i,curr=''):
            if i==len(word):
                if curr:    d[curr]+=1
                return 
            trv(word,i+1,curr+word[i])
            trv(word,i+1,curr)
        for w in strs:
            trv(w,0,'')
        return max([len(w) for w,f in d.items() if f==1],default=-1)