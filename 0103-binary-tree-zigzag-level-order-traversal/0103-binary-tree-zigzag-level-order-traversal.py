# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res, level = [], 0
        q.append(root)
        if not root:
            return []
        
        while q:
            subres= []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                subres.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
            if subres:
                if level % 2:
                    res.append(subres)
                else:
                    res.append(subres[::-1])
        return res