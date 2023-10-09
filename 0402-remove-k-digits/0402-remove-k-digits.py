class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in num:
            while stack and k > 0 and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)

        stack = stack[:len(stack) - k]
        res = "".join(stack).lstrip('0')
        return res if res else "0"
