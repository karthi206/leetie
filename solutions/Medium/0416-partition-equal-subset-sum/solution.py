# ──────────────────────────────────────────────────
# Problem  : 416. Partition Equal Subset Sum
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
# Link     : https://leetcode.com/problems/partition-equal-subset-sum/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19240000 (beats 86%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        le=len(A)
        l=[0]*(le)
        for i in range(2,le):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                l[i]=1+l[i-1]
        return sum(l)