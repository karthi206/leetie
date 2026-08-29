# ──────────────────────────────────────────────────
# Problem  : 2948. Make Lexicographically Smallest Array by Swapping Elements
# Difficulty: Medium
# Tags     : Array, Union-Find, Sorting
# Link     : https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19480000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        
        elements = [(nums[i], i) for i in range(n)]
        
        elements.sort()
        
        answer = [0] * n
        
        start = 0 
        
        while start < n:
            end = start
            
            while (
                end + 1 < n
                and elements[end + 1][0] - elements[end][0] <= limit
            ):
                end += 1
            
            indices = []
            
            for i in range(start, end + 1):
                indices.append(elements[i][1])
            
            indices.sort()
            
            for i, index in enumerate(indices):
                answer[index] = elements[start + i][0]
            
            start = end + 1
        
        return answer