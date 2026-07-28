class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []

        for i in s:
            if i in parentheses.values():
                stack.append(i)
            
            if i in parentheses and stack == []:
                return False
            
            if i in parentheses:
                if stack[-1] == parentheses[i]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        
        return False