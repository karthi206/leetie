# ──────────────────────────────────────────────────
# Problem  : 475. Heaters
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Sorting
# Link     : https://leetcode.com/problems/heaters/
# Runtime  : 31 ms (beats 59%)
# Memory   : 22472000 (beats 55%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    import bisect
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(houses)
        m = len(heaters)
        heaters.sort()
        ans = 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)

            if index==0:
                nearest_heater_distance = heaters[0] - house
            elif index==m:
                nearest_heater_distance = house - heaters[-1]
            else:
                nearest_heater_distance = min(heaters[index]-house, house - heaters[index-1])
            ans = max(ans, nearest_heater_distance)
        return ans