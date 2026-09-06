# ──────────────────────────────────────────────────
# Problem  : 402. Remove K Digits
# Difficulty: Medium
# Tags     : String, Stack, Greedy, Monotonic Stack
# Link     : https://leetcode.com/problems/remove-k-digits/
# Runtime  : 19 ms (beats 79%)
# Memory   : 20508000 (beats 32%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k > 0, remove remaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack
        
        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Handle edge case where result might be empty
        return result if result else '0'                