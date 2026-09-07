# ──────────────────────────────────────────────────
# Problem  : 457. Circular Array Loop
# Difficulty: Medium
# Tags     : Array, Hash Table, Two Pointers, Floyd's Cycle Finding Algorithm
# Link     : https://leetcode.com/problems/circular-array-loop/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19420000 (beats 27%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: return True
                    if i in visited: break          # credit to @crazyhyz, add this condition to avoid revisited
                    visited.add(i)
                    local_s.add(i)
                    prev, i = i, (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0): break
        return False