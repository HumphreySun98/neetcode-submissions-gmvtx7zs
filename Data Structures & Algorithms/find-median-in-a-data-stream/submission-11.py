class MedianFinder:

    def __init__(self):
        self.nums = []

        

    def addNum(self, num: int) -> None:
        self.nums.append(num)

        

    def findMedian(self) -> float:
        heap = list(self.nums)
        heapq.heapify(heap)
        length = len(heap)

        last = None
        for _ in range(length // 2):
            last = heapq.heappop(heap)
        
        if length % 2:
            return float(heap[0])
        else:
            return (heap[0] + last) /2
        