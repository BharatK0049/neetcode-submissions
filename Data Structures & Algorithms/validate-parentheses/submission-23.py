class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:

            if i in parentheses:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == parentheses[i]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(i)
        
        return stack == []
            
            
