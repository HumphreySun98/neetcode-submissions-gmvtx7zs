class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res= []

        for x,y in points:
            dis = x*x + y*y
            heap.append((dis,x,y))
        
        heapq.heapify(heap)

        for i in range(k):
            dis,x,y = heapq.heappop(heap)
            res.append([x,y])

        return res



        
        