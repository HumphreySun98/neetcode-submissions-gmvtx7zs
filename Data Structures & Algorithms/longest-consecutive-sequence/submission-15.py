class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        current = 0
        l = 0

        for num in seen:
            if num -1 not in seen:
                current = num
                l = 1


            while current+1 in seen:
                current += 1
                l += 1

            longest = max(longest,l)


        return longest


        