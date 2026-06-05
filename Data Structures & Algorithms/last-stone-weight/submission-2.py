class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = - heapq.heappop(heap)
            x = - heapq.heappop(heap)


            if x != y:
                heapq.heappush(heap,-(y - x))

        if not heap:
            return 0

        else:
            return -heap[0]

        
        