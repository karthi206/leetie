# ──────────────────────────────────────────────────
# Problem  : 648. Replace Words
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Trie
# Link     : https://leetcode.com/problems/replace-words/
# Runtime  : 291 ms (beats 16%)
# Memory   : 27448000 (beats 95%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        roots = set(dict)
        words = sentence.split()
        result = []

        for word in words:
            for i in range(len(word) + 1):
                prefix = word[:i]
                if prefix in roots:
                    result.append(prefix)
                    break
            else:
                result.append(word)

        return ' '.join(result)