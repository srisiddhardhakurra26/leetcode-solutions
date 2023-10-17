# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        if not root:
            return []
        
        while q:
            qLen = len(q)
            subres = []
            for i in range(qLen):
                node = q.popleft()
                subres.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if subres:
                res.append(subres[-1])
        return res