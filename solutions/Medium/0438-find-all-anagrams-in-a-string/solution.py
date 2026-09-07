# ──────────────────────────────────────────────────
# Problem  : 438. Find All Anagrams in a String
# Difficulty: Medium
# Tags     : Hash Table, String, Sliding Window
# Link     : https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Runtime  : 1442 ms (beats 11%)
# Memory   : 20024000 (beats 16%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,k,pz = len(s),len(p),Counter(p)
        return n>=k and [i-k for i,z in enumerate(accumulate(range(n),
            lambda z,i:z+Counter({s[i]:1})+Counter({s[i-k]:i>=k and -1}),
                initial=Counter())) if z==pz] or []