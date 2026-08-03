class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 :
            return False


        target = total // 2

        memo = {}

        def dfs(i,cur):

            if (i,cur) in memo:
                return memo[i,cur]
            
            if cur == target:
                return True

            if cur > target or i == len(nums):
                return False


            res = dfs(i+1,cur) or dfs(i+1,cur + nums[i])
            memo[i,cur] = res
            return res

        return dfs(0,0)


        