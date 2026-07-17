class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        # Sort cars by descending order to see which car is closest to target
        cars = list(zip(position, speed))
        cars_desc = sorted(cars, key=lambda car:car[0])

        current_time = 0
        for i in range(len(cars_desc)-1, -1, -1):
            finish_time = (target - cars_desc[i][0]) / cars_desc[i][1]

            if finish_time > current_time:
                fleet_count += 1
                current_time = finish_time

        return fleet_count