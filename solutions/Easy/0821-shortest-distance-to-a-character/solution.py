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
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a,n=[],len(s)
        for i in range(n):
            if s[i]==c:
                a.append(i)
        answer=[]
        j=0
        for i in range(n):
            if s[i]==c:
                answer.append(0)
                j+=1
            elif i<a[0]:
                answer.append(a[0]-i)
            elif i>a[-1]:
                answer.append(i-a[-1])
            else:
                answer.append(min((a[j]-i),(i-a[j-1])))
        return answer