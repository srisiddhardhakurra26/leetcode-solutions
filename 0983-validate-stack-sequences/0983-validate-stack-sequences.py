class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        push, pop = 1, 0
        stack.append(pushed[0])
        if len(pushed) != len(popped):
            return False
        
        while push < len(pushed) or pop < len(popped):
            if stack and stack[-1] == popped[pop]:
                stack.pop()
                pop += 1
            elif stack and stack[-1] != popped[pop] and push == len(pushed):
                return False
            else:
                stack.append(pushed[push])
                push += 1
        return True
        