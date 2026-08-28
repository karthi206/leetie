# ──────────────────────────────────────────────────
# Problem  : 860. Lemonade Change
# Difficulty: Easy
# Tags     : Array, Greedy
# Link     : https://leetcode.com/problems/lemonade-change/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19380000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False
        
        five_dollers = 0
        ten_dollers = 0

        for x in bills:
            if x == 5:
                five_dollers += 1
            elif x == 10:
                if five_dollers > 0:
                    five_dollers -= 1
                else:
                    return False
                ten_dollers += 1
            else:
                if five_dollers > 0 and ten_dollers > 0:
                    five_dollers -= 1
                    ten_dollers -= 1
                elif five_dollers > 2 :
                    five_dollers -= 3
                else:
                    return False
            print(five_dollers, ten_dollers)
        return True