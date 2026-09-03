# ──────────────────────────────────────────────────
# Problem  : 331. Verify Preorder Serialization of a Binary Tree
# Difficulty: Medium
# Tags     : String, Stack, Tree, Binary Tree
# Link     : https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19236000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        degree = 1
        for node in preorder.split(','):
            degree -= 1 
            
            if degree < 0: 
                return False
            
            if node != '#': 
                degree += 2 
        return degree == 0