class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        res = ""
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        while stack:
            res += stack.pop()
        return res[::-1]