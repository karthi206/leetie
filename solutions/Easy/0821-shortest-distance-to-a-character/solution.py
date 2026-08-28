# ──────────────────────────────────────────────────
# Problem  : 821. Shortest Distance to a Character
# Difficulty: Easy
# Tags     : Array, Two Pointers, String
# Link     : https://leetcode.com/problems/shortest-distance-to-a-character/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19280000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def shortestToChar(self, s, c):
        ans = []
        n = len(s)
        ptr1 = 0
        while ptr1 < n and s[ptr1] != c:
            ptr1 += 1
        idx = 0
        for idx in range(ptr1 + 1):
            ans.append(abs(idx - ptr1))
        ptr2 = 0
        while ptr2 < n:
            while ptr1 < n and s[ptr1] != c:
                ptr1 += 1
            ptr2 = ptr1 + 1
            while ptr2 < n and s[ptr2] != c:
                ptr2 += 1
            while idx < n and idx <= ptr2:
                if ptr2 < n:
                    ans.append(min(abs(idx - ptr1), abs(idx - ptr2)))
                else:
                    ans.append(abs(idx - ptr1))
                idx += 1
            ptr1 = ptr2
        return ans