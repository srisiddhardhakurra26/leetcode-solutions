# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary(nums, start, end):
            if start <= end:
                mid = start + (end - start) // 2
                node = TreeNode(nums[mid])
                node.left = binary(nums, start, mid - 1)
                node.right = binary(nums, mid + 1, end)
                return node
        return binary(nums, 0, len(nums) - 1)
        
