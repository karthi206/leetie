# ──────────────────────────────────────────────────
# Problem  : 498. Diagonal Traverse
# Difficulty: Medium
# Tags     : Array, Matrix, Simulation
# Link     : https://leetcode.com/problems/diagonal-traverse/
# Runtime  : 10 ms (beats 66%)
# Memory   : 21472000 (beats 81%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []
        row = col = 0

        for _ in range(m * n):
            result.append(matrix[row][col])

            if (row + col) % 2 == 0:
                if col == n - 1:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return result