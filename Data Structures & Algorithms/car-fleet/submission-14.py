class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Using stack
        stack = []
        # Sort cars by descending order to see which car is closest to target
        cars = list(zip(position, speed))
        cars_desc = sorted(cars, key=lambda car:car[0])

        for i in range(len(cars_desc)-1, -1, -1):
            time = (target - cars_desc[i][0]) / cars_desc[i][1]
            stack.append(time)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)