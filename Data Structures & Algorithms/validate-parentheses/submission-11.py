class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for i in s:
            if i in parenthesis and len(stack) == 0:
                return False

            # Pop
            if i in parenthesis:
                if parenthesis[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        # Checking
        if len(stack) == 0:
            return True
        else:
            return False