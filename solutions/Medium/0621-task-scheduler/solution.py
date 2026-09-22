# ──────────────────────────────────────────────────
# Problem  : 621. Task Scheduler
# Difficulty: Medium
# Tags     : Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
# Link     : https://leetcode.com/problems/task-scheduler/
# Runtime  : 21 ms (beats 77%)
# Memory   : 20712000 (beats 67%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        freq = list(Counter(tasks).values())
        maxF = max(freq)
        cnt = freq.count(maxF)
        return max(len(tasks), (maxF - 1) * (n + 1) + cnt)