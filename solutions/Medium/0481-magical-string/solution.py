# ──────────────────────────────────────────────────
# Problem  : 481. Magical String
# Difficulty: Medium
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/magical-string/
# Runtime  : 50 ms (beats 67%)
# Memory   : 19880000 (beats 73%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def magicalString(self, n: int) -> int:
        printOne = True
        if n < 4: return 1
        i = 2
        s = [1,2,2]
        onesCount = 1
        while i < n:
            # Look up what to append, and how many
            count = s[i]
            toAppend = 1 if printOne else 2
            # Print count * toAppends
            for _ in range(count):
                s.append(toAppend)
                # print(f"Appended {toAppend}, s: {s}")
                if toAppend == 1:
                    onesCount += 1
                if len(s) == n: return onesCount
            # Flip char each time
            printOne = not printOne
            i += 1
        return onesCount