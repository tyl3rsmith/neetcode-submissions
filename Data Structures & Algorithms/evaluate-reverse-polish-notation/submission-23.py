class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for t in tokens:
            if t not in '+-/*':
                numbers.append(int(t))
            
            if t == '+':
                r, l = numbers.pop(), numbers.pop()
                numbers.append(l + r)
            elif t == '-':
                r, l = numbers.pop(), numbers.pop()
                numbers.append(l - r)
            elif t == '/':
                r, l = numbers.pop(), numbers.pop()
                numbers.append(int(l / r))
            elif t == '*':
                r, l = numbers.pop(), numbers.pop()
                numbers.append(l * r)
    
        return numbers[-1]


