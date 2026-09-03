# ──────────────────────────────────────────────────
# Problem  : 334. Increasing Triplet Subsequence
# Difficulty: Medium
# Tags     : Array, Greedy, Longest Increasing Subsequence
# Link     : https://leetcode.com/problems/increasing-triplet-subsequence/
# Runtime  : 11 ms (beats 95%)
# Memory   : 38876000 (beats 67%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def increasingTriplet(self, nums):
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            if n <= min1:
                min1 = n  # Update first minimum
            elif n <= min2:
                min2 = n  # Update second minimum
            else:
                return True  # Found a third number greater than both
        return False  # No triplet found