class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+" and len(stack) >= 2:
                temp = list(stack)
                first = temp.pop()
                second = temp.pop()
                total = first + second
                stack.append(total)
            elif i == "D":
                stack.append(2 * stack[-1])
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)
