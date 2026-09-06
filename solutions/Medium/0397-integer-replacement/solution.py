# ──────────────────────────────────────────────────
# Problem  : 397. Integer Replacement
# Difficulty: Medium
# Tags     : Dynamic Programming, Greedy, Bit Manipulation, Memoization
# Link     : https://leetcode.com/problems/integer-replacement/
# Runtime  : 3 ms (beats 20%)
# Memory   : 19068000 (beats 100%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    # please upvote :)
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or n % 4 == 1:
                    n -= 1
                else:
                    n += 1
            cnt += 1
        return cnt