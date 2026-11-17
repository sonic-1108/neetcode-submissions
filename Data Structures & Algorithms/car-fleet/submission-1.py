class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = list(zip(position, speed))
        car.sort(reverse = True)
        max_time = 0
        result = 0
        for i in car:
            p = i[0]
            s = i[1]
            time = (target - p) / s
            if time > max_time:
                result += 1
                max_time = time
        return result