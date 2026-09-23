# ──────────────────────────────────────────────────
# Problem  : 592. Fraction Addition and Subtraction
# Difficulty: Medium
# Tags     : Math, String, Simulation, Euclidean Algorithm, Greatest Common Divisor
# Link     : https://leetcode.com/problems/fraction-addition-and-subtraction/
# Runtime  : 3 ms (beats 17%)
# Memory   : 19328000 (beats 77%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den
        
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}"