# ──────────────────────────────────────────────────
# Problem  : 535. Encode and Decode TinyURL
# Difficulty: Medium
# Tags     : Hash Table, String, Design, Hash Function
# Link     : https://leetcode.com/problems/encode-and-decode-tinyurl/
# Runtime  : 52 ms (beats 22%)
# Memory   : 19304000 (beats 37%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Codec:

    def __init__(self):
        self.map = {}
        self.id = 0
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        self.id += 1

        short = str(self.id)

        self.map[short] = longUrl

        return self.base + short

    def decode(self, shortUrl: str) -> str:
        short = shortUrl.split("/")[-1]

        return self.map[short]