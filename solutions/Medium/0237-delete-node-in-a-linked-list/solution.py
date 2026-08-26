# ──────────────────────────────────────────────────
# Problem  : 237. Delete Node in a Linked List
# Difficulty: Medium
# Tags     : Linked List
# Link     : https://leetcode.com/problems/delete-node-in-a-linked-list/
# Runtime  : 34 ms (beats 99%)
# Memory   : 19484000 (beats 67%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next

        ## alternative, one liner
        # node.val, node.next = node.next.val, node.next.nex't