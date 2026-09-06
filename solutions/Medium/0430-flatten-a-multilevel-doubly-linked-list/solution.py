# ──────────────────────────────────────────────────
# Problem  : 430. Flatten a Multilevel Doubly Linked List
# Difficulty: Medium
# Tags     : Linked List, Depth-First Search, Doubly-Linked List
# Link     : https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# Runtime  : 53 ms (beats 22%)
# Memory   : 19984000 (beats 31%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        curr = head
        while curr:
            if curr.child:
                nxt = curr.next
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None
                while curr.next:
                    curr = curr.next
                if nxt:
                    curr.next = nxt
                    nxt.prev = curr
            curr = curr.next
        return head