class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Remove excess zeros at the end of nums1
        nums1[m:] = []

        # Merge nums2 into nums1
        nums1[m:m+n] = nums2

        # Sort the merged nums1 in-place
        nums1.sort()
