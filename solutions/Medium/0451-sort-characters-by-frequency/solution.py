# ──────────────────────────────────────────────────
# Problem  : 451. Sort Characters By Frequency
# Difficulty: Medium
# Tags     : Hash Table, String, Sorting, Heap (Priority Queue), Bucket Sort, Counting
# Link     : https://leetcode.com/problems/sort-characters-by-frequency/
# Runtime  : 7 ms (beats 80%)
# Memory   : 20280000 (beats 41%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        pq = [(-freq, char) for char, freq in counter.items()]
        heapq.heapify(pq)
        result = ''
        while pq:
            freq, char = heapq.heappop(pq)
            result += char * -freq
        return result

