# ──────────────────────────────────────────────────
# Problem  : 532. K-diff Pairs in an Array
# Difficulty: Medium
# Tags     : Array, Hash Table, Two Pointers, Binary Search, Sorting
# Link     : https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Runtime  : 7 ms (beats 50%)
# Memory   : 20680000 (beats 55%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt=0
        c=Counter(nums)
        
        if k==0:
            for key,v in c.items():
                if v>1:
                    cnt+=1
        else:
            for key,v in c.items():
                if key+k in c:
                    cnt+=1
        return cnt