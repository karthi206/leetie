# ──────────────────────────────────────────────────
# Problem  : 649. Dota2 Senate
# Difficulty: Medium
# Tags     : String, Greedy, Queue
# Link     : https://leetcode.com/problems/dota2-senate/
# Runtime  : 9 ms (beats 89%)
# Memory   : 19744000 (beats 16%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()
        n = len(senate)

        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            r_idx = r.popleft()
            d_idx = d.popleft()

            if r_idx < d_idx:
                r.append(r_idx + n)
            else:
                d.append(d_idx + n)

        return "Radiant" if r else "Dire"