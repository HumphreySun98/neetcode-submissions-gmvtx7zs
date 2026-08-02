class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 :
            return False


        target = total // 2

        def dfs(i,cur):
            if cur == target:
                return True

            if cur > target or i == len(nums):
                return False


            if dfs(i+1,nums[i] + cur):
                return True

            if dfs(i+1,cur):
                return True


            return False

        return dfs(0,0)


        