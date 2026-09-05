# ──────────────────────────────────────────────────
# Problem  : 3904. Smallest Stable Index II
# Difficulty: Medium
# Tags     : Array, Prefix Sum
# Link     : https://leetcode.com/problems/smallest-stable-index-ii/
# Runtime  : 126 ms (beats 93%)
# Memory   : 33244000 (beats 24%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def firstStableIndex(self, A: List[int], k: int) -> int:
        msf = -1
        cand = cm = 0

        for i, x in enumerate(A):
            msf = max(msf, x)

            if i == cand:
                cm = msf

            if x < cm - k:
                cand = i + 1

        return cand if cand < len(A) else -1