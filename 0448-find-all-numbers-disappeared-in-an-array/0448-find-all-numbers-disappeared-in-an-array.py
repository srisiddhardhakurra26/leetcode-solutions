class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numset = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in numset:
                res.append(i)
        return res
