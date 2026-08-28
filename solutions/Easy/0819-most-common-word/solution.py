# ──────────────────────────────────────────────────
# Problem  : 819. Most Common Word
# Difficulty: Easy
# Tags     : Array, Hash Table, String, Counting
# Link     : https://leetcode.com/problems/most-common-word/
# Runtime  : 1 ms (beats 74%)
# Memory   : 19456000 (beats 23%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        word_count = {}
        i, n = 0, len(paragraph)

        while i < n:
            while i < n and not paragraph[i].isalpha():
                i += 1
            temp = []
            while i < n and paragraph[i].isalpha():
                temp.append(paragraph[i].lower())
                i += 1
            word = "".join(temp)
            if word and word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1

        max_word = ""
        max_freq = 0
        for w, f in word_count.items():
            if f > max_freq:
                max_freq = f
                max_word = w
        return max_word