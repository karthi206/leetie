# ──────────────────────────────────────────────────
# Problem  : 85. Maximal Rectangle
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
# Link     : https://leetcode.com/problems/maximal-rectangle/
# Runtime  : 2077 ms (beats 5%)
# Memory   : 22920000 (beats 99%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        M = len(matrix)
        N = len(matrix[0])

        # Convert characters to integers
        for i in range(M):
            for j in range(N):
                matrix[i][j] = int(matrix[i][j])

        # Row-wise prefix widths
        for i in range(M):
            for j in range(1, N):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i][j - 1]

        Ans = 0

        # Fix each column
        for j in range(N):
            for i in range(M):
                width = matrix[i][j]
                if width == 0:
                    continue

                # Expand downward
                currWidth = width
                k = i
                while k < M and matrix[k][j] > 0:
                    currWidth = min(currWidth, matrix[k][j])
                    height = k - i + 1
                    Ans = max(Ans, currWidth * height)
                    k += 1
                currWidth = width
                k = i
                while k >= 0 and matrix[k][j] > 0:
                    currWidth = min(currWidth, matrix[k][j])
                    height = i - k + 1
                    Ans = max(Ans, currWidth * height)
                    k -= 1

        return Ans