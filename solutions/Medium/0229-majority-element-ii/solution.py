# ──────────────────────────────────────────────────
# Problem  : 229. Majority Element II
# Difficulty: Medium
# Tags     : Array, Hash Table, Sorting, Counting, Boyer–Moore Majority Vote Algorithm
# Link     : https://leetcode.com/problems/majority-element-ii/
# Runtime  : 7 ms (beats 66%)
# Memory   : 23796000 (beats 11%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # Create a Counter to store the count of each element
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        # Iterate through the element count to identify majority elements
        for element, count in element_count.items():
            # Check if the element count is greater than the threshold
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements