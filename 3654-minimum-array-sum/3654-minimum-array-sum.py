class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)
        nums.sort()

        m1, m2 = bisect_left(nums, k), bisect_left(nums, 2*k-1)

        # Preparation for the corner case of swapping pairs
        candidates, swapCnt = set(), 0

        # Phase 1
        # Largest numbers, apply op1 then op2
        i = n-1
        while i >= m2 and op1 > 0:
            nums[i] = (nums[i]+1) // 2
            op1 -= 1
            if op2 > 0:
                nums[i] -= k
                op2 -= 1
            i -= 1

        # Phase 2
        # Apply op2 in the middle section, from left to right
        j = m1
        while j <= i and op2 > 0:
            if k % 2 == 1 and nums[j] % 2 == 0:
                # k odd and nums[j] even, could be swapped
                candidates.add(j)

            nums[j] -= k
            op2 -= 1
            j += 1

        # Phase 3
        # Apply op1 to the numbers in the middle section that haven't been applied op2
        while i >= j and op1 > 0:
            if k % 2 == 1 and nums[i] % 2 == 1:
                # k odd and nums[i] odd, could be swapped
                swapCnt += 1
            
            nums[i] = (nums[i]+1) // 2
            op1 -= 1
            i -= 1

        # Phase 4
        # Sort the remaining numbers and apply op1 greedily
        arr = sorted((nums[idx], idx) for idx in range(j))
        while op1 > 0:
            num, idx = arr.pop()
            nums[idx] = (num+1) // 2
            op1 -= 1

            if idx in candidates and swapCnt > 0:
                # Swapping pair
                swapCnt -= 1
                nums[idx] -= 1

        return sum(nums)