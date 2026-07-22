class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1,1
        for n in nums:
            tem = n * curmax
            curmax = max(n,tem,curmin*n)
            curmin = min(n,tem,curmin*n)


            res = max(curmax,res)


        return res
        