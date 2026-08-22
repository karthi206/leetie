# ──────────────────────────────────────────────────
# Problem  : 117. Populating Next Right Pointers in Each Node II
# Difficulty: Medium
# Tags     : Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Runtime  : 54 ms (beats 42%)
# Memory   : 20444000 (beats 26%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        q = deque([root])
        
        while q:
            totalNodes = len(q)
            
            for i in range(totalNodes):
                currNode = q.popleft()
                
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                currNode.next = q[0] if (i + 1 < totalNodes) else None
                
        return root