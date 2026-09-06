# ──────────────────────────────────────────────────
# Problem  : 419. Battleships in a Board
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Matrix
# Link     : https://leetcode.com/problems/battleships-in-a-board/
# Runtime  : 3 ms (beats 57%)
# Memory   : 21108000 (beats 52%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "X":
                    if (i == 0 or board[i - 1][j] == ".") and\
                       (j == 0 or board[i][j - 1] == "."):
                            count += 1
                            
        return count