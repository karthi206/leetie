# ──────────────────────────────────────────────────
# Problem  : 210. Course Schedule II
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort
# Link     : https://leetcode.com/problems/course-schedule-ii/
# Runtime  : 1 ms (beats 83%)
# Memory   : 20192000 (beats 98%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == numCourses else []