class Solution:
    def findMin(self, nums: List[int]) -> int:
        left  = 0
        right = len(nums)-1
        ans = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid +1
            else:
                right = mid -1
                ans = min(ans, nums[mid])
        return ans
        