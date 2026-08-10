class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(i,remain):
            
            if (i,remain) in memo:
                return memo[(i,remain)]
            if remain == 0:
                return 1
            if i >= n or remain < 0 :
                return 0

            use = dfs(i, remain - coins[i])
            skip =dfs(i+1,remain)

            memo[(i,remain)] = use + skip
            return memo[(i,remain)]
        return dfs(0,amount)