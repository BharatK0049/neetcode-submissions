class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ")":"(", 
            "}":"{", 
            "]":"["
        }

        # Edge case: starts with closing bracket
        if s[0] in brackets.keys():
            return False

        for i in s:
            # Pushing the opening bracket in the stack
            if i in brackets.values():
                stack.append(i)
            
            if i in brackets and len(stack) == 0:
                return False

            if i in brackets: 
                if brackets[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        
        print(stack)

        if len(stack) == 0:
            return True
        else:
            return False
