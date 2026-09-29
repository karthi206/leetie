# ──────────────────────────────────────────────────
# Problem  : 650. 2 Keys Keyboard
# Difficulty: Medium
# Tags     : Math, Dynamic Programming
# Link     : https://leetcode.com/problems/2-keys-keyboard/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19320000 (beats 48%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        steps = 0
        factor = 2
        
        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
            
        return steps