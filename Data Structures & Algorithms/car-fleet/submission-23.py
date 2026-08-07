class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = []

        cars = list(zip(position, speed))
        cars_desc = sorted(cars, key=lambda car:car[0], reverse=True)

        for i in range(len(cars_desc)):
            finishSpeed = (target - cars_desc[i][0]) / cars_desc[i][1]
            fleets.append(finishSpeed)
            
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()

        return len(fleets)       
