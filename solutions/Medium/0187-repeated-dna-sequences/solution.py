# ──────────────────────────────────────────────────
# Problem  : 187. Repeated DNA Sequences
# Difficulty: Medium
# Tags     : Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function, Z Algorithm, Boyer–Moore String-Search Algorithm
# Link     : https://leetcode.com/problems/repeated-dna-sequences/
# Runtime  : 801 ms (beats 13%)
# Memory   : 34104000 (beats 6%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        res = []
        n = len(s)
        count = {}

        for right in range(9, n):
            curr = s[left:right+1]
            if curr not in count:
                count[curr] = 1
            else:
                if count[curr] == 1:
                    res.append(curr[:])
                    count[curr] += 1
            left += 1
        return res