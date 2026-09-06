# ──────────────────────────────────────────────────
# Problem  : 417. Pacific Atlantic Water Flow
# Difficulty: Medium
# Tags     : Array, Depth-First Search, Breadth-First Search, Matrix
# Link     : https://leetcode.com/problems/pacific-atlantic-water-flow/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19412000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x, y, visited)

        pacific, atlantic = set(), set()
        for j in range(n): dfs(0, j, pacific)
        for i in range(m): dfs(i, 0, pacific)
        for j in range(n): dfs(m-1, j, atlantic)
        for i in range(m): dfs(i, n-1, atlantic)
        return list(pacific & atlantic)