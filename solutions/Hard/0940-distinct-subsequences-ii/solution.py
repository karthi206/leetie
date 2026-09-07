# ──────────────────────────────────────────────────
# Problem  : 940. Distinct Subsequences II
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/distinct-subsequences-ii/
# Runtime  : 7 ms (beats 90%)
# Memory   : 19172000 (beats 92%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007
        
        dp = 1
        last = [0] * 26
        
        for ch in s:
            index = ord(ch) - ord('a')
            
            old_dp = dp
            
            dp = (2 * dp - last[index] + MOD) % MOD
            
            last[index] = old_dp
        
        return (dp - 1 + MOD) % MOD