class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        missing_in_nums1 = []
        missing_in_nums2 = []
        
        for i in nums1:
            found = False
            for j in nums2:
                if i == j:
                    found = True
                    break
            if not found and i not in missing_in_nums2:
                missing_in_nums2.append(i)
        
        for i in nums2:
            found = False
            for j in nums1:
                if i == j:
                    found = True
                    break
            if not found and i not in missing_in_nums1:
                missing_in_nums1.append(i)
        
        return [missing_in_nums2, missing_in_nums1]
