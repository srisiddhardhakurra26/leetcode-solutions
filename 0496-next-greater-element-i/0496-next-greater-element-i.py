class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            for k in range(j + 1, len(nums2)):
                if nums2[j] < nums2[k]:
                    res[i] = nums2[k]
                    break
        return res
                