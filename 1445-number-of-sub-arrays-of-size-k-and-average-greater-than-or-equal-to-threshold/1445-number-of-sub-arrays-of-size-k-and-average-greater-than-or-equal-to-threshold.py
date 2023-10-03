class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        total, res = 0, 0
        avg = 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                avg = total // k
                if avg >= threshold:
                    res += 1
                total -= arr[l]
                l += 1
            total += arr[r]
        if (total // k) >= threshold:
            res += 1
        return res