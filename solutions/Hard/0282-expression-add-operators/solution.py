# ──────────────────────────────────────────────────
# Problem  : 282. Expression Add Operators
# Difficulty: Hard
# Tags     : Math, String, Backtracking
# Link     : https://leetcode.com/problems/expression-add-operators/
# Runtime  : 107 ms (beats 0%)
# Memory   : 19452000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        res = []
        def dfs(i, path, cur_num, prevNum):
            if i == len(s):
                if cur_num == target:
                    res.append(path)
                return
            
            for j in range(i, len(s)):
                # starting with zero?
                if j > i and s[i] == '0':
                    break
                num = int(s[i:j+1])

                # if cur index is 0 then simple add that number
                if i == 0:
                    dfs(j + 1, path + str(num), cur_num + num, num)
                else:
                    dfs(j + 1, path + "+" + str(num), cur_num + num, num)
                    dfs(j + 1, path + "-" + str(num), cur_num - num, -num)
                    dfs(j + 1, path + "*" + str(num), cur_num - prevNum + prevNum * num, prevNum * num)
        
        dfs(0, "", 0, 0)
        return res
        