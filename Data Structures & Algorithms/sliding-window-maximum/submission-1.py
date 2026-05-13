class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        cur_max = nums[0]
        cur_max_idx = 0
        
        for i in range(len(nums)):
            left = i - k + 1   # 当前窗口的左边界
            
            # 加入新元素:比当前 max 大就更新
            if nums[i] >= cur_max:
                cur_max = nums[i]
                cur_max_idx = i
            
            # 检查 cur_max 是否过期(滑出窗口)
            if cur_max_idx < left:
                # 在窗口 [left, i] 里重新找 max
                cur_max = nums[left]
                cur_max_idx = left
                for j in range(left + 1, i + 1):
                    if nums[j] >= cur_max:
                        cur_max = nums[j]
                        cur_max_idx = j
            
            # 窗口装满后开始记答案
            if i >= k - 1:
                result.append(cur_max)
        
        return result