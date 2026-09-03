# ──────────────────────────────────────────────────
# Problem  : 363. Max Sum of Rectangle No Larger Than K
# Difficulty: Hard
# Tags     : Array, Binary Search, Matrix, Prefix Sum, Ordered Set
# Link     : https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
# Runtime  : 498 ms (beats 83%)
# Memory   : 20216000 (beats 14%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])
        for i in range(n):
            lstSum = [0] * m
            for j in range(i, n):
                currSum = 0
                curlstSum = [0]
                for t in range(m):
                    lstSum[t] += matrix[t][j]
                    currSum += lstSum[t]
                    pos = bisect_left(curlstSum, currSum - k)
                    if pos < len(curlstSum):
                        if curlstSum[pos] == currSum - k:
                            return k
                        else:
                            ans = max(ans, currSum - curlstSum[pos])
                    insort(curlstSum, currSum)
        return ans