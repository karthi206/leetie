# ──────────────────────────────────────────────────
# Problem  : 832. Flipping an Image
# Difficulty: Easy
# Tags     : Array, Two Pointers, Bit Manipulation, Matrix, Simulation
# Link     : https://leetcode.com/problems/flipping-an-image/
# Runtime  : 3 ms (beats 11%)
# Memory   : 19372000 (beats 23%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            start = 0
            end = len(image[0]) - 1
            while(start < end):
                image[i][start], image[i][end] = image[i][end], image[i][start]
                start += 1
                end -= 1
        
        for i in range(len(image)):
            start = 0
            while(start < len(image[0])):
                if(image[i][start] == 1):
                    image[i][start] = 0
                else:
                    image[i][start] = 1
                start += 1
        return image