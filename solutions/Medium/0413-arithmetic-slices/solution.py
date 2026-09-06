# ──────────────────────────────────────────────────
# Problem  : 413. Arithmetic Slices
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Sliding Window
# Link     : https://leetcode.com/problems/arithmetic-slices/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19328000 (beats 0%)
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