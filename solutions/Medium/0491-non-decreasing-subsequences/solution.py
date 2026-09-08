# ──────────────────────────────────────────────────
# Problem  : 491. Non-decreasing Subsequences
# Difficulty: Medium
# Tags     : Array, Hash Table, Backtracking, Bit Manipulation
# Link     : https://leetcode.com/problems/non-decreasing-subsequences/
# Runtime  : 23 ms (beats 39%)
# Memory   : 29016000 (beats 21%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def solve(self, nums, index, output, ans):
        # base case: if we have reached the end of the input array
        if index >= len(nums):
            # only add the output if it has more than one element
            if len(output) > 1:
                ans.add(tuple(output))
            return
        
        # if the output is empty or the current element is greater than or equal to the last element in the output
        if not output or nums[index] >= output[-1]:
            # add the current element to the output and recursively call solve
            output.append(nums[index])
            self.solve(nums, index+1, output, ans)
            # remove the last element from the output before returning
            output.pop()
        
        # recursively call solve without adding the current element to the output
        self.solve(nums, index+1, output, ans)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # use a set to store the unique sub sequences
        ans = set()
        self.solve(nums, 0, [], ans)
        return [list(x) for x in ans]