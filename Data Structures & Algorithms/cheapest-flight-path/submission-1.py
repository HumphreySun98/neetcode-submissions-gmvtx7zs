class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        heap =[(0,src,0)]
        best ={}


        while heap:
            cost,s,stop = heapq.heappop(heap)
            if s == dst:
                return cost

            if stop > k:
                continue

            if s in best and best[s] <= stop:
                continue

            best[s] = stop
            for nei,c in graph[s]:
                heapq.heappush(heap,(c+cost,nei,stop+1))


        return -1

        