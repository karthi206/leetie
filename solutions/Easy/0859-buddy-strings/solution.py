# ──────────────────────────────────────────────────
# Problem  : 859. Buddy Strings
# Difficulty: Easy
# Tags     : Hash Table, String
# Link     : https://leetcode.com/problems/buddy-strings/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19268000 (beats 67%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)

        if len(goal) != n:
            return False

        if s == goal:
            temp = set(s)
            return len(temp) < len(goal)  

        i = 0
        j = n - 1

        while i < j and s[i] == goal[i]:
            i += 1

        while j >= 0 and s[j] == goal[j]:
            j -= 1

        if i < j:
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s = ''.join(s_list)

        return s == goal