# ──────────────────────────────────────────────────
# Problem  : 443. String Compression
# Difficulty: Medium
# Tags     : Two Pointers, String
# Link     : https://leetcode.com/problems/string-compression/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19296000 (beats 88%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans