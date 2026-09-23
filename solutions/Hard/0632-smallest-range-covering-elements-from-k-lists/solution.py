# ──────────────────────────────────────────────────
# Problem  : 632. Smallest Range Covering Elements from K Lists
# Difficulty: Hard
# Tags     : Array, Hash Table, Greedy, Sliding Window, Sorting, Heap (Priority Queue)
# Link     : https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Runtime  : 238 ms (beats 60%)
# Memory   : 42036000 (beats 73%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        cur_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0)) 
            cur_max = max(cur_max, nums[i][0])
        small = [float('-inf'), float('inf')]
        while heap:
            cur_min, list_idx, i = heapq.heappop(heap)
            if cur_max - cur_min < small[1] - small[0]:
                small = [cur_min, cur_max]
            if i + 1 < len(nums[list_idx]):
                nxt = nums[list_idx][i + 1]
                heapq.heappush(heap, (nxt, list_idx, i+1))
                cur_max = max(cur_max, nxt)
            else:
                break
        return small