# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append([root, 0])
        res = 0

        while q:
            subres = []
            qLen = len(q)
            for _ in range(qLen):
                node, i = q.popleft()
                subres.append(i)
                if node.left:
                    q.append([node.left, i * 2])
                if node.right:
                    q.append([node.right, i * 2 + 1])
            res = max(res, max(subres) - min(subres) + 1)
        return res