# ──────────────────────────────────────────────────
# Problem  : 297. Serialize and Deserialize Binary Tree
# Difficulty: Hard
# Tags     : String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
# Link     : https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Runtime  : 92 ms (beats 40%)
# Memory   : 22668000 (beats 44%)
# Language : python3
# Copyright: (c) 2026 karthi206. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Codec:
    def serialize(self, root):
        if not root: return "null"
        res, q = [], deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ','.join(res)

    def deserialize(self, data):
        if data == "null": return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            curr = q.popleft()
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1
        return root