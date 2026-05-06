class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        ans = max(piles)  

        def hours_need(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            return hours


        while left <= right :
            k = (left + right) // 2
            if hours_need(k) <= h:
                right = k -1
                ans = min(ans, k)
            else:
                
                left = k +1

        return ans
        