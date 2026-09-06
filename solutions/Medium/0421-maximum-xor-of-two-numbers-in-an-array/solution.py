# ──────────────────────────────────────────────────
# Problem  : 421. Maximum XOR of Two Numbers in an Array
# Difficulty: Medium
# Tags     : Array, Hash Table, Bit Manipulation, Trie
# Link     : https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Runtime  : 5440 ms (beats 16%)
# Memory   : 458560000 (beats 30%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class TrieNode:
    def __init__(self):
        self.children = [None, None]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root

        for i in range(30, -1, -1):
            b = (num >> i) & 1

            if node.children[b] is None:
                node.children[b] = TrieNode()

            node = node.children[b]

    def mXor(self, num):
        node = self.root
        op = 0

        for i in range(30, -1, -1):
            b = (num >> i) & 1
            o = 1 - b

            if node.children[o] is not None:
                op |= (1 << i)
                node = node.children[o]
            else:
                node = node.children[b]

        return op


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()

        for i in nums:
            t.insert(i)

        op = 0

        for i in nums:
            op = max(op, t.mXor(i))

        return op