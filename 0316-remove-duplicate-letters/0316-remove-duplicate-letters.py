class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOccurance = {} #s -> count
        visited = set() 
        stack = []
        
        for i, c in enumerate(s):
            lastOccurance[c] = i

        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and s[i] < stack[-1] and i < lastOccurance.get(stack[-1], -1):
                visited.remove(stack.pop())
            visited.add(s[i])
            stack.append(s[i])
        return ''.join(stack)