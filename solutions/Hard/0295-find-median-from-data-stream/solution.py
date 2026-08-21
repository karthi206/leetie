# ──────────────────────────────────────────────────
# Problem  : 295. Find Median from Data Stream
# Difficulty: Hard
# Tags     : Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
# Link     : https://leetcode.com/problems/find-median-from-data-stream/
# Runtime  : 268 ms (beats 13%)
# Memory   : 42356000 (beats 30%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n//2]
        return (self.arr[n//2] + self.arr[n//2-1]) / 2