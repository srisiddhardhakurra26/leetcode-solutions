class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(l, r, arr):
            if l == r:
                return arr
            
            m = (l + r) // 2
            mergeSort(l, m, arr)
            mergeSort(m + 1, r, arr)
            merge(arr, l, m, r)
            return arr
        
        return mergeSort(0, len(nums) - 1, nums)