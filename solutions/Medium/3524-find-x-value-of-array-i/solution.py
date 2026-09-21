# ──────────────────────────────────────────────────
# Problem  : 3524. Find X Value of Array I
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming
# Link     : https://leetcode.com/problems/find-x-value-of-array-i/
# Runtime  : 310 ms (beats 87%)
# Memory   : 34268000 (beats 53%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            x = num % k
            nxt = [0] * k
            nxt[x] += 1

            for r in range(k):
                new_r = (r * x) % k
                nxt[new_r] += dp[r]

            for r in range(k):
                ans[r] += nxt[r]
            dp = nxt

        return ans