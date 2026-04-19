class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_item = sorted(count.items(), key = lambda x:x[1], reverse = True)
        return[iterm[0] for iterm in sorted_item[:k]]