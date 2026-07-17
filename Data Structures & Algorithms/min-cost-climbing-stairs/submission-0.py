class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(n - 1,-1, -1):
        
            skip1 = dp[i+1]
            if i + 2 <= n:

                skip2 = dp[i+2]
            else:
                skip2 = 0
            dp[i] = cost[i] + min(skip1,skip2)

        return min(dp[0],dp[1])

        