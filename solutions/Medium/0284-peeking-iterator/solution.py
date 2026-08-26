# ──────────────────────────────────────────────────
# Problem  : 284. Peeking Iterator
# Difficulty: Medium
# Tags     : Array, Design, Iterator
# Link     : https://leetcode.com/problems/peeking-iterator/
# Runtime  : 51 ms (beats 0%)
# Memory   : 19400000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.current = self.iterator.next() if self.iterator.hasNext() else None        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.current
        

    def next(self):
        """
        :rtype: int
        """
        value = self.current
        self.current = self.iterator.next() if self.iterator.hasNext() else None       
        return value
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.current != None
      