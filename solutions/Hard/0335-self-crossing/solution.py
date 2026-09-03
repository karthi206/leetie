# ──────────────────────────────────────────────────
# Problem  : 335. Self Crossing
# Difficulty: Hard
# Tags     : Array, Math, Geometry
# Link     : https://leetcode.com/problems/self-crossing/
# Runtime  : 39 ms (beats 63%)
# Memory   : 29160000 (beats 92%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
  def isSelfCrossing(self, x: List[int]) -> bool:
    # If there are less than 4 values in the array, the path can't cross itself
    if len(x) <= 3:
      return False

    # Loop through the array starting from the 3rd index
    for i in range(3, len(x)):
      # Case 1: current line crosses the line 3 steps before it
      #           _______
      #         |      |
      #         |      |
      # ________|______| <-- current line
      #         |          |
      #         |          |
      #         |__________| <-- line 3 steps before
      if x[i - 2] <= x[i] and x[i - 1] <= x[i - 3]:
        return True
      
      # Case 2: current line crosses the line 4 steps before it
      #         _____
      #        |      |
      #        |      |
      #        |      |________
      #        |               |
      #        |               |
      #        |_______________| <-- current line
      #              line 4 steps before
      if i >= 4 and x[i - 1] == x[i - 3] and x[i - 2] <= x[i] + x[i - 4]:
        return True
      
      # Case 3: current line crosses the line 5 steps before it
      #         ______
      #        |      |
      #        |      |
      #        |______| <-- line 5 steps before
      #               |
      #               |
      #         ______|_______
      #        |              |
      #        |              |
      #        |______________| <-- current line
      if i >= 5 and x[i - 4] <= x[i - 2] and x[i - 2] <= x[i] + x[i - 4] and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5]:
        return True

    # If no crossing has been found, the path does not cross itself
    return False