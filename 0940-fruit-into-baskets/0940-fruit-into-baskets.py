class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = {}
        total, res, l = 0, 0, 0

        for r in range(len(fruits)):
            hm[fruits[r]] = 1 + hm.get(fruits[r], 0)
            total += 1

            while len(hm) > 2:
                if fruits[l] in hm:
                    hm[fruits[l]] -= 1
                    if hm[fruits[l]] == 0:
                        hm.pop(fruits[l])

                l += 1
                total -= 1
            res = max(res, total)
        return res