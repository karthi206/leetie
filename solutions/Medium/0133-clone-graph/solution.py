# ──────────────────────────────────────────────────
# Problem  : 133. Clone Graph
# Difficulty: Medium
# Tags     : Hash Table, Depth-First Search, Breadth-First Search, Graph Theory
# Link     : https://leetcode.com/problems/clone-graph/
# Runtime  : 46 ms (beats 79%)
# Memory   : 19860000 (beats 18%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]