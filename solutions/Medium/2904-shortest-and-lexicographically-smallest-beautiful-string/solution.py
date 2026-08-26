# ──────────────────────────────────────────────────
# Problem  : 2904. Shortest and Lexicographically Smallest Beautiful String
# Difficulty: Medium
# Tags     : String, Sliding Window
# Link     : https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
# Runtime  : 19 ms (beats 6%)
# Memory   : 19304000 (beats 31%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)

        for i in range(n):

            oneCnt = 0
            cur = ""

            for j in range(i, n):

                cur += s[j]

                if s[j] == '1':
                    oneCnt += 1

                # More than k ones can never become valid again
                if oneCnt > k:
                    break

                if oneCnt == k:
                    if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                        ans = cur

        return ans