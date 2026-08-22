# ──────────────────────────────────────────────────
# Problem  : 236. Lowest Common Ancestor of a Binary Tree
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor
# Link     : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Runtime  : 129 ms (beats 74%)
# Memory   : 50800000 (beats 45%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right        