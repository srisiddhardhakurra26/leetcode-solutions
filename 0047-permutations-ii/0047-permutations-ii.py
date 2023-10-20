class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, subres = [], []
        count = collections.Counter(nums)

        def dfs():
            if len(subres) == len(nums):
                res.append(subres.copy())
                return
            
            for c in count:
                if count[c] > 0:
                    subres.append(c)
                    count[c] -= 1
                    dfs()
                    subres.pop()
                    count[c] += 1
        dfs()
        return res
