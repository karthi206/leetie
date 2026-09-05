# ──────────────────────────────────────────────────
# Problem  : 382. Linked List Random Node
# Difficulty: Medium
# Tags     : Linked List, Math, Reservoir Sampling, Randomized
# Link     : https://leetcode.com/problems/linked-list-random-node/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19276000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        reservoir = self.head.val
        
        i = 2
        next = self.head.next
        while next:
            if random.random() < 1/i:
                reservoir = next.val
                
            i += 1
            next = next.next
            
        return reservoir