# ──────────────────────────────────────────────────
# Problem  : 393. UTF-8 Validation
# Difficulty: Medium
# Tags     : Array, Bit Manipulation
# Link     : https://leetcode.com/problems/utf-8-validation/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19236000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        #Solution1 (BruteForce)
        count = 0 #Count of remaining follow-on bytes to check
        for n in data:
            if count>0:
                if n>>6==0b10:
                    count -=1
                else:
                    return False #Invalid pattern so returning immediately
            else:
                if n>>7==0b0:
                    count = 0 #1 Byte found
                elif n>>5==0b110:
                    count = 1 #2 Bytes found
                elif n>>4==0b1110:
                    count = 2 #3 Bytes found
                elif n>>3==0b11110:
                    count = 3 #4 Bytes found
                else:
                    return False
        
        return True if count==0 else False