class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        far = 0


        for i in range(n):
            if i > far : 
                return False


            far = max(i + nums[i],far)
            if far >= n-1:
                return True
