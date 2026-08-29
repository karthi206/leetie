# ──────────────────────────────────────────────────
# Problem  : 319. Bulb Switcher
# Difficulty: Medium
# Tags     : Math, Brainteaser
# Link     : https://leetcode.com/problems/bulb-switcher/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19028000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**(1/2))