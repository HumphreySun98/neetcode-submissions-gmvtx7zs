class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        n = len(nums)

        for i in range(n):
            prod = 1
            for j in range(i,n):
                prod *= nums[j]

                res = max(res,prod)


        return res
        