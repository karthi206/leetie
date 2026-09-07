# ──────────────────────────────────────────────────
# Problem  : 24. Swap Nodes in Pairs
# Difficulty: Medium
# Tags     : Linked List, Recursion
# Link     : https://leetcode.com/problems/swap-nodes-in-pairs/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19204000 (beats 62%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first,second=head,head.next
        first.next=self.swapPairs(second.next)
        second.next=first
        return second

        