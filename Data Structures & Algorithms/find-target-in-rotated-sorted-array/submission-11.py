class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1

        if ans == 0:
            l = 0
            r = len(nums) - 1
        elif target >= nums[0]:
            l = 0
            r = ans - 1
        else:
            l = ans
            r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m

        return -1