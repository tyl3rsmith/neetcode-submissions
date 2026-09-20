class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack approach
        # we maintain a stack
        # for each token if its an operand push it onto the stack
        # if its an operator we take the top 2 elements on the stack and apply the operand
        # we store the result back on the stack
        # at the end the stack should have only one element which is our result

        stack = []
        for i in range(len(tokens)):
            if tokens[i] in '+-/*':
                b, a = stack.pop(), stack.pop()

                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '-':
                    stack.append(a - b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]