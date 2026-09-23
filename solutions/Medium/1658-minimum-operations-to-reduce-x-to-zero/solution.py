# ──────────────────────────────────────────────────
# Problem  : 1658. Minimum Operations to Reduce X to Zero
# Difficulty: Medium
# Tags     : Array, Hash Table, Binary Search, Sliding Window, Prefix Sum
# Link     : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Runtime  : 97 ms (beats 40%)
# Memory   : 30652000 (beats 93%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        k = sum(A) - x
        if k < 0: return -1 
        best = -1
        
        s = i = 0
        
        for j, num in enumerate(A):
            s += num
            while s > k:
                s -= A[i]
                i += 1  
            if s == k:
                best = max(best, j - i + 1)

        return -1 if best < 0 else len(A) - best
