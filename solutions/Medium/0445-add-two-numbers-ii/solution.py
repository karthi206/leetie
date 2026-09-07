# ──────────────────────────────────────────────────
# Problem  : 445. Add Two Numbers II
# Difficulty: Medium
# Tags     : Linked List, Math, Stack
# Link     : https://leetcode.com/problems/add-two-numbers-ii/
# Runtime  : 6 ms (beats 42%)
# Memory   : 19272000 (beats 82%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def helper(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummyHead.next
        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        ans = self.helper(l1, l2)
        return self.reverseList(ans)