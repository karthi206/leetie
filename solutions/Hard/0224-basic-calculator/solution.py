# ──────────────────────────────────────────────────
# Problem  : 224. Basic Calculator
# Difficulty: Hard
# Tags     : Math, String, Stack, Recursion
# Link     : https://leetcode.com/problems/basic-calculator/
# Runtime  : 37 ms (beats 60%)
# Memory   : 20148000 (beats 88%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
  def calculate(self, s: str) -> int:
    ans = 0
    num = 0
    sign = 1
    stack = [sign] 
    for c in s:
      if c.isdigit():
        num = num * 10 + int(c)
      elif c == '(':
        stack.append(sign)
      elif c == ')':
        stack.pop()
      elif c == '+' or c == '-':
        ans += sign * num
        sign = (1 if c == '+' else -1) * stack[-1]
        num = 0
    return ans + sign * num