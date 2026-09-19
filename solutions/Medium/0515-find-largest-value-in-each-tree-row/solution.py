# ──────────────────────────────────────────────────
# Problem  : 515. Find Largest Value in Each Tree Row
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Runtime  : 0 ms (beats 0%)
# Memory   : 19344000 (beats 0%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        q = deque()
        q.append(root)

        while q:
            max_val = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)                    

            res.append(max_val)

        return res