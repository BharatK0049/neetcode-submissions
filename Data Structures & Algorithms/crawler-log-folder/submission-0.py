class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in logs:
            
            if stack != []:
                if i == "../":
                    stack.pop()
                elif i == './':
                    continue
                else:
                    stack.append(i)
            else:
                if i == '../' or i == './':
                    continue
                else:
                    # Append x/
                    stack.append(i)

        return len(stack)