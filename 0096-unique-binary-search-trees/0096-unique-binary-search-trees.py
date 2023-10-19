class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                left, right = root - 1, node - root
                total += numTree[left] * numTree[right]
            numTree[node] = total
        return numTree[n]