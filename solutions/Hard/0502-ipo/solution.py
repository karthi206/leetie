# ──────────────────────────────────────────────────
# Problem  : 502. IPO
# Difficulty: Hard
# Tags     : Array, Greedy, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/ipo/
# Runtime  : 248 ms (beats 81%)
# Memory   : 45064000 (beats 88%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        i = 0
        maximizeCapital = []
        while k > 0:
            while i < n and projects[i][0] <= w:
                heapq.heappush(maximizeCapital, -projects[i][1])
                i += 1
            if not maximizeCapital:
                break
            w -= heapq.heappop(maximizeCapital)
            k -= 1
        return w