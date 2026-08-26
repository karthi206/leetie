# ──────────────────────────────────────────────────
# Problem  : 208. Implement Trie (Prefix Tree)
# Difficulty: Medium
# Tags     : Hash Table, String, Design, Trie
# Link     : https://leetcode.com/problems/implement-trie-prefix-tree/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19428000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Fixed size array for 'a' to 'z'
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return True