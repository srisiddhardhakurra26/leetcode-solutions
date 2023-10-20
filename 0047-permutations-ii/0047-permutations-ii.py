class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, subres, hm = [], [], {}

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
        
        def dfs():
            if len(subres) == len(nums):
                res.append(subres.copy())
                return
            
            for n in hm:
                if hm[n] > 0:
                    subres.append(n)
                    hm[n] -= 1
                    
                    dfs()

                    subres.pop()
                    hm[n] += 1
        dfs()
        return res