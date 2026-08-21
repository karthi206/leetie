# ──────────────────────────────────────────────────
# Problem  : 3116. Kth Smallest Amount With Single Denomination Combination
# Difficulty: Hard
# Tags     : Array, Math, Binary Search, Bit Manipulation, Combinatorics, Number Theory
# Link     : https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
# Runtime  : 167 ms (beats 30%)
# Memory   : 20864000 (beats 22%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for mask in range(1, 1 << n):
            size = 0
            cur_lcm = 1
            for i in range(n):
                if (mask >> i) & 1:
                    size += 1
                    cur_lcm = math.lcm(cur_lcm, coins[i])
            subsets.append((cur_lcm, size))
            
        def count_amounts_le(x: int) -> int:
            total = 0
            for lcm_val, size in subsets:
                if size % 2 == 1:
                    total += x // lcm_val
                else:
                    total -= x // lcm_val
            return total
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_amounts_le(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans