# ──────────────────────────────────────────────────
# Problem  : 432. All O`one Data Structure
# Difficulty: Hard
# Tags     : Hash Table, Linked List, Design, Doubly-Linked List
# Link     : https://leetcode.com/problems/all-oone-data-structure/
# Runtime  : 9090 ms (beats 5%)
# Memory   : 35088000 (beats 15%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class AllOne:
    def __init__(self):
        self.myDict = {}

    def inc(self, key: str) -> None:
        if key in self.myDict:
            self.myDict[key] += 1
        else:
            self.myDict[key] = 1

    def dec(self, key: str) -> None:
        if key in self.myDict:
            if self.myDict[key] > 1:
                self.myDict[key] -= 1
            else:
                self.myDict.pop(key)

    def getMaxKey(self) -> str:
        if not self.myDict:
            return ""
        maxVal = max(self.myDict.values())
        for key in self.myDict.keys():
            if self.myDict[key] == maxVal:
                return key

    def getMinKey(self) -> str:
        if not self.myDict:
            return ""
        minVal = min(self.myDict.values())
        for key in self.myDict.keys():
            if self.myDict[key] == minVal:
                return key
