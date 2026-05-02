class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p,s in zip(position,speed):
            t = (target-p)/s
            cars.append((p,t))

        cars.sort(reverse = True)
        fleet = 0
        cur_time = 0
        for p, t in cars:
            if cur_time < t:
                fleet += 1
                cur_time = t
        return fleet

        