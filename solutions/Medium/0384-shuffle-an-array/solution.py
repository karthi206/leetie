# ──────────────────────────────────────────────────
# Problem  : 384. Shuffle an Array
# Difficulty: Medium
# Tags     : Array, Math, Design, Randomized
# Link     : https://leetcode.com/problems/shuffle-an-array/
# Runtime  : 14 ms (beats 66%)
# Memory   : 23472000 (beats 34%)
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