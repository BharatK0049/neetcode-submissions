class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            stack.append(i)

            while len(stack) >= 2:
                # only if top is negative and second last is positive do they collide, if vice versa, they go in opposite directions
                if (stack[-1] < 0 and stack[-2] > 0):
                    if (stack[-1] + stack[-2]) == 0:
                        stack.pop()
                        stack.pop()
                    elif (stack[-1] + stack[-2]) > 0:
                        stack.pop()
                    else:
                        stack.pop(-2)
                else:
                    break
            
                
            
        return stack