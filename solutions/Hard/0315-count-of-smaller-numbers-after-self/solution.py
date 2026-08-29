# ──────────────────────────────────────────────────
# Problem  : 315. Count of Smaller Numbers After Self
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
# Link     : https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Runtime  : 2631 ms (beats 13%)
# Memory   : 36616000 (beats 86%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = []
        
        # Process from right to left ⬅️
        for num in reversed(nums):
            # Find insertion position using binary search 🔍
            insert_pos = bisect.bisect_left(sorted_nums, num)
            result.append(insert_pos)
            # Insert into the sorted list to maintain order
            bisect.insort(sorted_nums, num)
        
        # Reverse to get the correct order 🔄
        return result[::-1]