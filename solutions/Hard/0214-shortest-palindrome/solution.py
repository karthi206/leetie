# ──────────────────────────────────────────────────
# Problem  : 214. Shortest Palindrome
# Difficulty: Hard
# Tags     : String, Rolling Hash, String Matching, Hash Function, Manacher, Z Algorithm, Knuth–Morris–Pratt Algorithm
# Link     : https://leetcode.com/problems/shortest-palindrome/
# Runtime  : 48 ms (beats 64%)
# Memory   : 23352000 (beats 51%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        count = self.kmp(s[::-1], s)
        return s[count:][::-1] + s
    def kmp(self, txt: str, patt: str) -> int:
        new_string = patt + '#' + txt
        pi = [0] * len(new_string)
        i = 1
        k = 0
        while i < len(new_string):
            if new_string[i] == new_string[k]:
                k += 1
                pi[i] = k
                i += 1
            else:
                if k > 0:
                    k = pi[k - 1]
                else:
                    pi[i] = 0
                    i += 1
        return pi[-1]