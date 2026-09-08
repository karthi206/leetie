# ──────────────────────────────────────────────────
# Problem  : 466. Count The Repetitions
# Difficulty: Hard
# Tags     : Two Pointers, String, Dynamic Programming
# Link     : https://leetcode.com/problems/count-the-repetitions/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19384000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # Early exit if s1 is too small to contain s2
        if n1 == 0:
            return 0
        
        s1_count, s2_count, index = 0, 0, 0
        recall = {}

        # Process s1 n1 times
        while s1_count < n1:
            s1_count += 1
            for char in s1:
                if char == s2[index]:
                    index += 1
                if index == len(s2):
                    s2_count += 1
                    index = 0
            
            # Detect and handle loops
            if index in recall:
                prev_s1_count, prev_s2_count = recall[index]
                loop_s1_count = s1_count - prev_s1_count
                loop_s2_count = s2_count - prev_s2_count
                
                # Calculate how many times the loop can repeat
                remaining_loops = (n1 - s1_count) // loop_s1_count
                s1_count += remaining_loops * loop_s1_count
                s2_count += remaining_loops * loop_s2_count

            recall[index] = (s1_count, s2_count)
        
        return s2_count // n2