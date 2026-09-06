# ──────────────────────────────────────────────────
# Problem  : 394. Decode String
# Difficulty: Medium
# Tags     : String, Stack, Recursion
# Link     : https://leetcode.com/problems/decode-string/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19456000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0
        return self.decode(s)
    def decode(self, s: str) -> str:
        res, num = "", 0
        while self.i < len(s):
            c = s[self.i]
            if c.isdigit():
                num = num * 10 + int(c)
                self.i += 1
            elif c == '[':
                self.i += 1
                inner = self.decode(s)
                res += inner * num
                num = 0
            elif c == ']':
                self.i += 1
                return res
            else:
                res += c
                self.i += 1
        return res