class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = list(zip(position, speed))

        pos_speed = sorted(pos_speed, key=lambda x: x[0], reverse=True)

        current_time = 0
        no_fleets = 0
        for i in pos_speed:
            finish_time = (target - i[0]) / i[1]

            if finish_time > current_time:
                current_time = finish_time
                no_fleets += 1
        
        return no_fleets

