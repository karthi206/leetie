# ──────────────────────────────────────────────────
# Problem  : 207. Course Schedule
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort, Directed Acyclic Graph
# Link     : https://leetcode.com/problems/course-schedule/
# Runtime  : 0 ms (beats 100%)
# Memory   : 21052000 (beats 38%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)

        vis = [False] * numCourses
        path = [False] * numCourses

        def dfs(node):
            vis[node] = path[node] = True
            
            for next_node in adj[node]:
                if not vis[next_node]:
                    if dfs(next_node): return True
                elif path[next_node]: return True
            
            path[node] = False
            return False

        for i in range(numCourses):
            if not vis[i]:
                if dfs(i): return False

        return True