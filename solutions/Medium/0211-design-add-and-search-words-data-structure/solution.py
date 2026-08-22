# ──────────────────────────────────────────────────
# Problem  : 211. Design Add and Search Words Data Structure
# Difficulty: Medium
# Tags     : String, Depth-First Search, Design, Trie
# Link     : https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Runtime  : 968 ms (beats 60%)
# Memory   : 68500000 (beats 55%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True
        
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_word
               
            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                    
            if word[index] in node.children:
                return dfs(node.children[word[index]], index+1)
            
            return False
    
        return dfs(self.root, 0)