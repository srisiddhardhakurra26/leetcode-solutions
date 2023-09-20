class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rs = self.prefix[right + 1]
        ls = self.prefix[left]
        return rs - ls


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)