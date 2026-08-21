# ──────────────────────────────────────────────────
# Problem  : 68. Text Justification
# Difficulty: Hard
# Tags     : Array, String, Simulation
# Link     : https://leetcode.com/problems/text-justification/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19168000 (beats 97%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]