class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums)):
            nextdp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True

                nextdp.add(t + nums[i])
                nextdp.add(t)

            dp = nextdp

        return True if target in dp else False



