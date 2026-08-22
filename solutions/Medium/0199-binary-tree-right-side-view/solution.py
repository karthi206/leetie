# ──────────────────────────────────────────────────
# Problem  : 199. Binary Tree Right Side View
# Difficulty: Medium
# Tags     : Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Link     : https://leetcode.com/problems/binary-tree-right-side-view/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19120000 (beats 93%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [root]
        curr = 0
        ans = []
        
        while curr < len(queue):
            ans.append(queue[curr].val)
            qSize = len(queue)
            
            for i in range(curr, qSize):
                if queue[i].right:
                    queue.append(queue[i].right)
                if queue[i].left:
                    queue.append(queue[i].left)
            
            curr = qSize
        
        return ans