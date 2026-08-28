# ──────────────────────────────────────────────────
# Problem  : 804. Unique Morse Code Words
# Difficulty: Easy
# Tags     : Array, Hash Table, String
# Link     : https://leetcode.com/problems/unique-morse-code-words/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19148000 (beats 93%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dic = {}
        map_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        # a = 97
        # z = 122
        for i in range(97, 123):
            dic[chr(i)] = map_morse[i-97]
        
        diff = []
        for w in words:
            cur = ""
            for x in w:
                cur += dic[x]
            if cur not in diff: diff.append(cur)

        return len(diff)
        