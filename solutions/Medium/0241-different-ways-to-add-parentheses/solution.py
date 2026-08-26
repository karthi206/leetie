# ──────────────────────────────────────────────────
# Problem  : 241. Different Ways to Add Parentheses
# Difficulty: Medium
# Tags     : Math, String, Dynamic Programming, Recursion, Memoization, Bracket Sequences
# Link     : https://leetcode.com/problems/different-ways-to-add-parentheses/
# Runtime  : 3 ms (beats 36%)
# Memory   : 19536000 (beats 9%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        # ans = []
        for i in range(len(expression)):
            oper = expression[i]
            if oper == "+" or oper == "-" or oper == "*":
                sub_str1 = expression[0 : i]
                sub_str2 = expression[i + 1 : ]
                s1 = self.diffWaysToCompute(sub_str1)
                s2 = self.diffWaysToCompute(sub_str2)
                for i in s1:
                    for j in s2:
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))
        if len(res) == 0:
            res.append(int(expression))
        # print(res)
        return res