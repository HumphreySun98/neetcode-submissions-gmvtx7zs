class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(i,total):
            if (i,total) in memo:
                return memo[(i,total)]
            if i == n and total == target:
                return 1
            if i == n and total != target:
                return 0
            plus = dfs(i+1,total + nums[i])
            minus = dfs(i+1,total -  nums[i])
            memo[(i,total)] = plus + minus
            return plus + minus

        return dfs(0,0)
             
        