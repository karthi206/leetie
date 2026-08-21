# ──────────────────────────────────────────────────
# Problem  : 147. Insertion Sort List
# Difficulty: Medium
# Tags     : Linked List, Sorting
# Link     : https://leetcode.com/problems/insertion-sort-list/
# Runtime  : 389 ms (beats 61%)
# Memory   : 21192000 (beats 65%)
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
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head

        while current:
            nxt = current.next

            prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            current.next = prev.next
            prev.next = current

            current = nxt

        return dummy.next