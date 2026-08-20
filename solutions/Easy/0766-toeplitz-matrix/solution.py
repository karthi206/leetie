# ──────────────────────────────────────────────────
# Problem  : 766. Toeplitz Matrix
# Difficulty: Easy
# Tags     : Array, Matrix
# Link     : https://leetcode.com/problems/toeplitz-matrix/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19524000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
            for i in range(1,len(matrix)):
                for j in range(1,len(matrix[0])):
                    if matrix[i-1][j-1] != matrix[i][j]:
                        return False
            return True