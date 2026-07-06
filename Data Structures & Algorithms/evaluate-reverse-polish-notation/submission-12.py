class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in tokens:
            if i == '+':
                a = stack.pop()
                b = stack.pop()                
                result = b + a
                stack.append(result)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()                
                result = b * a
                stack.append(result)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()                
                result = int(b / a)
                stack.append(result)
            else:
                stack.append(int(i))
        
        return stack[-1]
