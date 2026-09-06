# ──────────────────────────────────────────────────
# Problem  : 388. Longest Absolute File Path
# Difficulty: Medium
# Tags     : String, Stack, Depth-First Search
# Link     : https://leetcode.com/problems/longest-absolute-file-path/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19204000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depth = 0
        longest = 0
        pathMap = { 0: 0 }

        lines = input.split("\n")

        for line in lines:
            name = line.lstrip("\t")
            depth = len(line) - len(name)

            if "." in name:
                longest = max(longest, pathMap[depth] + len(name))
            else:
                pathMap[depth + 1] = pathMap[depth] + len(name) + 1
        
        return longest