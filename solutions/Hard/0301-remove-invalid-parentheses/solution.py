# ──────────────────────────────────────────────────
# Problem  : 301. Remove Invalid Parentheses
# Difficulty: Hard
# Tags     : String, Backtracking, Breadth-First Search
# Link     : https://leetcode.com/problems/remove-invalid-parentheses/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19500000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(s):
            open= 0
            for i in range(len(s)):
                if s[i] == '(':
                    open += 1
                if s[i] == ')':
                    open -= 1
                if open < 0:
                    return False
            if open != 0:
                return False
            return True
        
        queue = deque([s])
        visited = set()
        visited.add(s)
        result = []
        found = False
        
        while queue:
            for _ in range(len(queue)):
                cur_s = queue.popleft()
                if is_valid(cur_s):
                    result.append(cur_s)
                    found = True
                if found:
                    continue
                
                for i in range(len(cur_s)):
                    if cur_s[i] =='(' or cur_s[i] == ')':
                        new_s = cur_s[:i] + cur_s[i+1 :]
                        if new_s not in visited:
                            visited.add(new_s)
                            queue.append(new_s)
            if found:
                return result
        return [""]