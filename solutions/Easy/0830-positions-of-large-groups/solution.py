# ──────────────────────────────────────────────────
# Problem  : 830. Positions of Large Groups
# Difficulty: Easy
# Tags     : String
# Link     : https://leetcode.com/problems/positions-of-large-groups/
# Runtime  : 3 ms (beats 34%)
# Memory   : 19352000 (beats 29%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        stack = [s[0]]
        s += "$"
        
        for i in range(1, len(s)):
            if s[i] != stack[-1] :
                if len(stack) >= 3:
                    ans.append([i-len(stack), i-1])
                
                stack = []

            stack.append(s[i])

        return ans