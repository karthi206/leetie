# ──────────────────────────────────────────────────
# Problem  : 382. Linked List Random Node
# Difficulty: Medium
# Tags     : Linked List, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/linked-list-random-node/
# Runtime  : 3 ms (beats 0%)
# Memory   : 19364000 (beats 0%)
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