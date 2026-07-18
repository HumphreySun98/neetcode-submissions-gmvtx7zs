class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]


        def robber(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]

            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0],houses[1])

            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+houses[i])


            return dp[n-1]



        return max(robber(nums[:-1]),robber(nums[1:]))



             