# ──────────────────────────────────────────────────
# Problem  : 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
# Difficulty: Hard
# Tags     : Two Pointers, String, Enumeration
# Link     : https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
# Runtime  : 22 ms (beats 61%)
# Memory   : 19620000 (beats 32%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        freq = Counter(s)
        
        def check() -> bool:
            return all(v >= 0 for v in freq.values())

        center = ''
        for x, v in freq.items():
            if v % 2 == 0: continue
            if center: return ""
            center = x
            freq[x] -= 1

        sz = len(s)
        half = sz // 2
        for i, w in enumerate(target[:half]):
            freq[w] -= 2

        if check():
            head = target[:half]
            tail = center + head[::-1]
            if tail > target[half:]:
                return head + tail

        for i in range(half - 1, -1, -1):
            w = target[i]
            freq[w] += 2
            if not check(): continue

            for j in range(ord(w) - ord('a') + 1, 26):
                x = ascii_lowercase[j]
                if freq[x] == 0: continue

                freq[x] -= 2
                result = list(target[:i + 1])
                result[i] = x

                for x in ascii_lowercase:
                    result.extend(x * (freq[x] // 2))

                tail = result[::-1]
                result.append(center)
                result += tail

                return ''.join(result)

        return ""