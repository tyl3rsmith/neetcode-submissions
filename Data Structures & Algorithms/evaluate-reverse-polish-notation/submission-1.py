class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in ops:
                stack.append(token)
            else:
                op = token
                num2 = int(stack.pop())
                num1 = int(stack.pop())

                if op == '+':
                    stack.append(num1 + num2)
                elif op == '-':
                    stack.append(num1 - num2)
                elif op == '*':
                    stack.append(num1 * num2)
                elif op == '/':
                    stack.append(int(num1 / num2))
        
        return int(stack[-1])
