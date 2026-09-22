# ──────────────────────────────────────────────────
# Problem  : 622. Design Circular Queue
# Difficulty: Medium
# Tags     : Array, Linked List, Design, Queue
# Link     : https://leetcode.com/problems/design-circular-queue/
# Runtime  : 11 ms (beats 26%)
# Memory   : 19784000 (beats 98%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1    
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        self.size -= 1    
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front]    

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[(self.rear - 1) % self.k]    

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()