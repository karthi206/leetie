# ──────────────────────────────────────────────────
# Problem  : 3622. Check Divisibility by Digit Sum and Product
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19284000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s, p, x=0, 1, n
        while x>0:
            x, r=divmod(x, 10)
            s+=r
            p*=r
        return n%(s+p)==0