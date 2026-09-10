class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r  = 0, len(heights)-1

        while l < r:
            width = r -l
            length = min(heights[l],heights[r])
            a = width * length

            res = max(res,a)
            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1


        return res
        