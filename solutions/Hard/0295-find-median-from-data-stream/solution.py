# ──────────────────────────────────────────────────
# Problem  : 295. Find Median from Data Stream
# Difficulty: Hard
# Tags     : Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
# Link     : https://leetcode.com/problems/find-median-from-data-stream/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19268000 (beats 92%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0