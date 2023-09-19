class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strset = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                if res in strset:
                    return None
                else:
                    return res
            res = backtrack(i + 1, cur)
            if res:
                return res
            
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res:
                return res
        return backtrack(0, ["0" for s in nums])