class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:        # ← 注意:seen 不是 seen()
                return num
            seen.add(num)
        