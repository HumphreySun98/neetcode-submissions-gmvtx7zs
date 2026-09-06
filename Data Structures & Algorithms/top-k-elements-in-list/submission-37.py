class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)

        for c,t in count.items():
            heapq.heappush(heap,(t,c))
            if len(heap) > k:
                heapq.heappop(heap)


        res = []

        for t,c in heap:
            res.append(c)


        return res




        