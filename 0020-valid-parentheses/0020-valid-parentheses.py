class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c not in hm:
                stack.append(c)
                continue
            if not stack:
                return False
            openP = stack.pop()
            if openP != hm[c]:
                return False
        return True if not stack else False