# ──────────────────────────────────────────────────
# Problem  : 624. Maximum Distance in Arrays
# Difficulty: Medium
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/maximum-distance-in-arrays/
# Runtime  : 26 ms (beats 71%)
# Memory   : 35500000 (beats 40%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance