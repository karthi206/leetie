# ──────────────────────────────────────────────────
# Problem  : 554. Brick Wall
# Difficulty: Medium
# Tags     : Array, Hash Table
# Link     : https://leetcode.com/problems/brick-wall/
# Runtime  : 3 ms (beats 93%)
# Memory   : 22796000 (beats 83%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_frequency = {} # HashMap to store the number of common edges among the rows
        max_frequency = 0 # Variable to store the frequency of most occuring edge
        
        for row in range(len(wall)): # Iterating through each row
            edge_postion = 0 # Variable to store different edge postion
            
            for brick_no in range(len(wall[row])-1): # Iterating through each brick inside a row
                current_brick_length = wall[row][brick_no] # Length of the current brick
                edge_postion = edge_postion + current_brick_length # Next Edge Position = Previous Edge Position + Current Brick's Length
                edge_frequency[edge_postion] = edge_frequency.get(edge_postion, 0) + 1 # Incrementing the Frequency of just calculated Edge Postion
                max_frequency = max(edge_frequency[edge_postion], max_frequency) # Comparing the "Frequency of just calculated Edge Postion" with "Max Frequency seen till now" & storing whichever is greater.
                
        return len(wall) - max_frequency # returning (Number of Bricks Crossed by Line) i.e. (Number of Rows in Wall - Frequency of Most Occuring Edge)