# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []
        if root:
            q.append(root)
        else:
            return []

        while q:
            subres = []
            for i in range(len(q)):
                node = q.popleft()
                subres.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)        
            res.append(max(subres))
        return res if root else []