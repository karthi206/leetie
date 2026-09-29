# ──────────────────────────────────────────────────
# Problem  : 652. Find Duplicate Subtrees
# Difficulty: Medium
# Tags     : Hash Table, Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/find-duplicate-subtrees/
# Runtime  : 8 ms (beats 37%)
# Memory   : 25192000 (beats 63%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    ans = []
    count = collections.Counter()

    def encode(root: Optional[TreeNode]) -> str:
      if not root:
        return ''

      encoded = str(root.val) + '#' + \
          encode(root.left) + '#' + \
          encode(root.right)
      count[encoded] += 1
      if count[encoded] == 2:
        ans.append(root)
      return encoded

    encode(root)
    return ans