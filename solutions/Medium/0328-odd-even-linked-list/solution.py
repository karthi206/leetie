# ──────────────────────────────────────────────────
# Problem  : 328. Odd Even Linked List
# Difficulty: Medium
# Tags     : Linked List
# Link     : https://leetcode.com/problems/odd-even-linked-list/
# Runtime  : 0 ms (beats 100%)
# Memory   : 21084000 (beats 77%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None : return head 
        odd = ListNode(0) 
        odd_ptr = odd
        even = ListNode(0)
        even_ptr = even 
        idx = 1 
        while head != None :
            if idx % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            head = head.next
            idx+=1
        even_ptr.next = None
        odd_ptr.next = even.next
        return odd.next