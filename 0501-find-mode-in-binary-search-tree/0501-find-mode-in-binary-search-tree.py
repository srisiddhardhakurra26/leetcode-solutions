# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        freq = {}

        while q:
            node = q.popleft()
            freq[node.val] = 1 + freq.get(node.val, 0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        max_freq = max(freq.values())
        res = [key for key, value in freq.items() if value == max_freq]

        return res   