# ──────────────────────────────────────────────────
# Problem  : 640. Solve the Equation
# Difficulty: Medium
# Tags     : Math, String, Simulation, Linear Algebra
# Link     : https://leetcode.com/problems/solve-the-equation/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19356000 (beats 54%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def solveEquation(self, equation):
        x = a = 0
        side = 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                x += side * int(sign + '1') * int(num or 1)
            elif num:
                a -= side * int(sign + num)
        return 'x=%d' % (a / x) if x else 'No solution' if a else 'Infinite solutions'