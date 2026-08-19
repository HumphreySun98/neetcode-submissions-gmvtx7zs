class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def reach(i):
            if i  == 0:
                return True


            for j in range(i):
                if j + nums[j] >= i and reach(j):
                    return True


            return False


        return reach(n-1)
        