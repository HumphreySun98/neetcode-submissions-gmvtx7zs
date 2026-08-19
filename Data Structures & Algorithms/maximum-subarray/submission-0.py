class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        cur = 0
        best = float('-INF')

        for right in range(len(nums)):
            cur += nums[right]

            best = max(best,cur)


            if cur < 0:
                cur = 0



        return best