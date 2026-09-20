class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in '+-*/':
                    num1 = int(tokens[i-2])
                    num2 = int(tokens[i-1])

                    if tokens[i] == '+':
                        result = num1 + num2
                    elif tokens[i] == '-':
                        result = num1 - num2
                    elif tokens[i] == '*':
                        result = num1 * num2
                    elif tokens[i] == '/':
                        result = int(num1 / num2)

                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])