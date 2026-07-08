class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        heap = [(0,k)]

        while heap:
            cur_dist, node = heapq.heappop(heap)
            if cur_dist > dist[node]:
                continue


            for nei, weight in graph[node]:
            
                new_dist = cur_dist + weight 
                if new_dist < dist[nei] :
                    dist[nei] = new_dist
                    heapq.heappush(heap,(new_dist,nei))


        ans  = max(dist[1:])


        if ans == float('inf'):
            return -1

        else :
            return ans 

            


        