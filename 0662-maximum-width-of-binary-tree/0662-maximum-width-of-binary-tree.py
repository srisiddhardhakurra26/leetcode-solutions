# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append([root, 1])
        res = 0

        while q:
            subres = []
            for _ in range(len(q)):
                node, heapValue = q.popleft()
                subres.append(heapValue)
                if node.left:
                    q.append([node.left, heapValue * 2])
                if node.right:
                    q.append([node.right, (heapValue * 2) + 1])
            res = max(res, max(subres) - min(subres) + 1)
        return res