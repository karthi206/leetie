# ──────────────────────────────────────────────────
# Problem  : 606. Construct String from Binary Tree
# Difficulty: Medium
# Tags     : String, Tree, Depth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/construct-string-from-binary-tree/
# Runtime  : 4 ms (beats 43%)
# Memory   : 20204000 (beats 97%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(root):
            if not root:
                return ''
            if root.right:
                return str(root.val) + '(' + dfs(root.left) + ')(' + dfs(root.right) + ')'
            if root.left:
                return str(root.val) + '(' + dfs(root.left) + ')'
            
            return str(root.val)
      
        return dfs(root)        