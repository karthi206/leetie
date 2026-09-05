# ──────────────────────────────────────────────────
# Problem  : 382. Linked List Random Node
# Difficulty: Medium
# Tags     : Linked List, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/linked-list-random-node/
# Runtime  : 15 ms (beats 65%)
# Memory   : 22876000 (beats 91%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────


class Solution:

    def __init__(self, head: ListNode):
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        i = random.randint(0, len(self.nodes) - 1)
        return self.nodes[i]