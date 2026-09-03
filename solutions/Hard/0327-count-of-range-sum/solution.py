# ──────────────────────────────────────────────────
# Problem  : 327. Count of Range Sum
# Difficulty: Hard
# Tags     : Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set, Treap
# Link     : https://leetcode.com/problems/count-of-range-sum/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19108000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        psum = [0]
        for num in nums:
            psum.append(psum[-1] + num)

        result, slist = 0, SortedList()
        for pval in reversed(psum):
            result += slist.bisect_right(pval + upper) - slist.bisect_left(pval + lower)
            slist.add(pval)

        return result