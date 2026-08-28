# ──────────────────────────────────────────────────
# Problem  : 299. Bulls and Cows
# Difficulty: Medium
# Tags     : Hash Table, String, Counting
# Link     : https://leetcode.com/problems/bulls-and-cows/
# Runtime  : 4 ms (beats 58%)
# Memory   : 19284000 (beats 73%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secretCount = [0] * 10
        guessCount = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secretCount[int(secret[i])] += 1
                guessCount[int(guess[i])] += 1

        cows = 0
        for digit in range(10):
            cows += min(secretCount[digit], guessCount[digit])

        return str(bulls) + "A" + str(cows) + "B"