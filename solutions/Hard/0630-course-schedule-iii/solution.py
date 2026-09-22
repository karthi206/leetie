# ──────────────────────────────────────────────────
# Problem  : 630. Course Schedule III
# Difficulty: Hard
# Tags     : Array, Greedy, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/course-schedule-iii/
# Runtime  : 41 ms (beats 81%)
# Memory   : 23208000 (beats 77%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []

        # 📅 Process courses by deadline
        courses.sort(key=lambda x: x[1])

        ans = 0
        current_day = 1

        for dur, dead_l in courses:

            # ✅ Course fits
            if current_day + dur - 1 <= dead_l:
                current_day += dur
                heappush(heap, -dur)
                ans += 1

            # ❌ Course doesn't fit → try replacement
            elif heap:
                d = -heap[0]  # 🏔️ Longest selected course

                if current_day - d + dur - 1 <= dead_l and dur <= d:
                    current_day -= d
                    current_day += dur

                    heappop(heap)
                    heappush(heap, -dur)

        return ans