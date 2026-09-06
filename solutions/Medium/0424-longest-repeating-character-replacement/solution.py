# ──────────────────────────────────────────────────
# Problem  : 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Tags     : Hash Table, String, Sliding Window
# Link     : https://leetcode.com/problems/longest-repeating-character-replacement/
# Runtime  : 83 ms (beats 60%)
# Memory   : 19784000 (beats 16%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            # track frequencies
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # more than k replacements needed then compress the window
            while (right-left+1) - max_freq > k:
                
                count[s[left]] -= 1
                left += 1

            # update answer in the current window
            answer = max(answer, right-left+1)

        return answer