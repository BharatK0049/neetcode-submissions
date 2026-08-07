class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        noFleets = 0

        pos_speeds = list(zip(position, speed))
        pos_speeds = sorted(pos_speeds, key=lambda x:x[0], reverse=True)

        currentSpeed = 0
        for i in range(len(pos_speeds)):
            calculatedSpeed = (target - pos_speeds[i][0]) / pos_speeds[i][1]

            if calculatedSpeed > currentSpeed:
                noFleets += 1
                currentSpeed = calculatedSpeed
        
        return noFleets
