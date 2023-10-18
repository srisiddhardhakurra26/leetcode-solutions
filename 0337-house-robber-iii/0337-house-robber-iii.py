# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0] #[withroot, withoutRoot]
            leftdfs = dfs(node.left)
            rightdfs = dfs(node.right)

            withRoot = node.val + leftdfs[1] + rightdfs[1]
            withoutRoot = max(leftdfs) + max(rightdfs)

            return [withRoot, withoutRoot]

        return max(dfs(root))