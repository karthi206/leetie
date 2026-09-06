# ──────────────────────────────────────────────────
# Problem  : 429. N-ary Tree Level Order Traversal
# Difficulty: Medium
# Tags     : Tree, Breadth-First Search
# Link     : https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Runtime  : 51 ms (beats 80%)
# Memory   : 20888000 (beats 93%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        lvls = []
        
        
        if not root:
            return lvls
        
        
        q = deque([root])
        
        
        while q:
            l = len(q)
            curr_lvl = []
            
            
            for _ in range(l):
                n = q.popleft()
                curr_lvl.append(n.val)
                
                
                for child in n.children:
                    q.append(child)
            
            
            lvls.append(curr_lvl)
        
        
        return lvls