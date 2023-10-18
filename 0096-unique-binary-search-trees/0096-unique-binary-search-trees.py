class Solution:
    def numTrees(self, n: int) -> int:
        cache = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            for i in range(0, node):
                left, right = i, node - i - 1
                total += cache[left] * cache[right]
            cache[node] = total
        return cache[n]