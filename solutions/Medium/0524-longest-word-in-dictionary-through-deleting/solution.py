# ──────────────────────────────────────────────────
# Problem  : 524. Longest Word in Dictionary through Deleting
# Difficulty: Medium
# Tags     : Array, Two Pointers, String, Sorting
# Link     : https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
# Runtime  : 227 ms (beats 31%)
# Memory   : 21436000 (beats 7%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        ans = ""

        for word in dictionary:

            i = 0
            j = 0

            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1

            if i == len(word):

                if len(word) > len(ans):
                    ans = word

                elif len(word) == len(ans) and word < ans:
                    ans = word

        return ans