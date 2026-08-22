# ──────────────────────────────────────────────────
# Problem  : 116. Populating Next Right Pointers in Each Node
# Difficulty: Medium
# Tags     : Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Runtime  : 55 ms (beats 0%)
# Memory   : 19508000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root : return None
        q=deque([root])
        while q:
            rightNode=None
            for _ in range(len(q)):
                cur=q.popleft()
                cur.next,rightNode=rightNode,cur
                if cur.right:
                    q.extend([cur.right,cur.left])
        return root   
        