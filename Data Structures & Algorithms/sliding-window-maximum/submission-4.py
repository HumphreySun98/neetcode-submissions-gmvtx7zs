class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        cur_max = 0
        cur_max_index = 0

        for i in range(len(nums)):
            left = i-k +1
            if nums [i] > cur_max:
                cur_max = nums[i]
                cur_max_index = i

            if left > cur_max_index:
                cur_max = nums[left]
                cur_max_index = left
                for j in range(left+1,i+1):
                    if nums[j] > cur_max:
                        cur_max = nums[j]
                        cur_max_index = j

            if i >= k -1:
                result.append(cur_max)

        return result

        
        