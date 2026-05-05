class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def hours_need(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours

        while left <= right:
            k = (left + right) // 2
            if hours_need(k) <= h:
                right = k-1
            else:
                left = k + 1
            
        return left
        