# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            subres = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    subres.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if subres:
                res.append(subres)

        return res 