class Solution:
    def isValid(self, s: str) -> bool:
        
        para = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for i in s:
            if i in para and len(stack) == 0:
                return False

            if i in para.values():
                stack.append(i)
            else:
                if stack[-1] == para[i]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False