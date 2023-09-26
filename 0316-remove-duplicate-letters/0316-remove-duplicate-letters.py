class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurance = {} #s -> count 
        stack = []
        
        for i, c in enumerate(s):
            lastOccurance[c] = i

        for i in range(len(s)):
            if s[i] in stack:
                continue
            while stack and s[i] < stack[-1] and i < lastOccurance[stack[-1]]:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)