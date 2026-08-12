class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dfs(i,buying):
            if i >= n:
                return 0

            if (i,buying) in memo:
                return memo[(i,buying)]
            skip = dfs(i+1, buying)
            buy = dfs(i+1,False) - prices[i]
            buy = max(skip,buy)
            sell = dfs(i+2,True) + prices[i]
            sell= max(skip,sell)
            if buying:
                memo[(i,buying)] = buy
                res = buy
                
            else:
                memo[(i,buying)] = sell
                res = sell
            memo[(i,buying)] = res

            return memo[(i,buying)]

        return dfs(0,True)


            
            
        