class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        sign = '+'
        s += '+'
        num = 0
        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)
            elif c in '+-/*':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)