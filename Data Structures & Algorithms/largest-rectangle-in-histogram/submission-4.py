class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area =0

        for i in range(n):
            h = heights[i]
            left = i
            while left > 0 and heights[left-1] >= h:
                left -= 1

            right = i
            while right < n-1 and heights[right+1] >= h:
                right +=1
            area = h * (right - left + 1)
            max_area = max(max_area, area)

        return max_area

        

        