class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
            
        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        total_left = (m + n +1)//2

        while left <= right:
            i = (left + right)//2
            j =total_left - i
            if i > 0:
                nums1_left = nums1[i-1]
            else:
                nums1_left = float('-inf')

            if j >0 :
                nums2_left = nums2[j-1]
            else:
                nums2_left = float('-inf')

            if i<m:
                nums1_right = nums1[i]
            else:
                nums1_right = float('inf')
                
            if j < n:
                nums2_right = nums2[j]
            else:
                nums2_right = float('inf')
                

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left,nums2_left)

                left_max = max(nums1_left,nums2_left)
                right_max = min(nums1_right,nums2_right)

                return (left_max + right_max)/2

            elif nums1_left > nums2_right:
                right = i-1

            else:
                left = i+1