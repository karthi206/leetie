# ──────────────────────────────────────────────────
# Problem  : 406. Queue Reconstruction by Height
# Difficulty: Medium
# Tags     : Array, Binary Indexed Tree, Segment Tree, Sorting
# Link     : https://leetcode.com/problems/queue-reconstruction-by-height/
# Runtime  : 6 ms (beats 29%)
# Memory   : 19624000 (beats 72%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output=[] 
        people.sort(key=lambda x: (-x[0], x[1]))                
        for a in people:
            output.insert(a[1], a)
        
        return output  