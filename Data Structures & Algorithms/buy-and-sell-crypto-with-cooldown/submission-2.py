class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        def dfs(i,buying):
            if i >= n :
                return 0

            if (i,buying) in memo:
                return memo[(i,buying)]
            skip = dfs(i+1,buying)
            if buying:
                buy = dfs(i+1,False) - prices[i]
                memo[(i,buying)] = max(skip,buy)
                return memo[(i,buying)]

            else:
                sell = dfs(i+2,True) + prices[i]
                memo[(i,buying)] = max(skip,sell)
                return memo[(i,buying)]

            

        return dfs(0,True)
        