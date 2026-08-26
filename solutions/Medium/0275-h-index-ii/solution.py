# ──────────────────────────────────────────────────
# Problem  : 275. H-Index II
# Difficulty: Medium
# Tags     : Array, Binary Search
# Link     : https://leetcode.com/problems/h-index-ii/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19152000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        left, right = 0, n
        while left<right:
            mid=left+(right-left)//2
            if citations[mid]>=n-mid:
                right=mid
            else:
                left=mid+1
        return n-left