class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if i % 2 == 0:
                res.append(i)
        for i in nums:
            if i % 2 == 1:
                res.append(i)
        return res