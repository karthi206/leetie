# ──────────────────────────────────────────────────
# Problem  : 486. Predict the Winner
# Difficulty: Medium
# Tags     : Array, Math, Dynamic Programming, Recursion, Minimax, Game Theory, Zero-Sum Game
# Link     : https://leetcode.com/problems/predict-the-winner/
# Runtime  : 7129 ms (beats 5%)
# Memory   : 19448000 (beats 36%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from decimal import *

class Solution(object):
    def smallestGoodBase(self, n):
        
        getcontext().prec = 26

        for m in range(60,1,-1):
            k=Decimal(2)
            for i in range(300):
                k = self.newtonMethod(k,m,int(n))
        
            basicRoundK = round(k)

            if (round(k,6)==basicRoundK and basicRoundK>1):
                return str(basicRoundK)

    def newtonMethod(self,k,m,n):
        numerator = (((k**m)-1)/(k-1))-n

        denominatorPt1 = m*(k-1)*(k**(m-1))-((k**m)-1)
        denominatorPt2 = (k-1)**2
        totalDenom = denominatorPt1/denominatorPt2

        return k - (numerator/totalDenom)