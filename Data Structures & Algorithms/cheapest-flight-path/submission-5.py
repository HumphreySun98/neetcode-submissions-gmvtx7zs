class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        dis = [INF]*n
        dis[src] = 0

        for _ in range(k+1):
            tem = dis[:]
            for u,v,w in flights:
                if dis[u] + w < tem[v]:
                    tem[v] = dis[u] + w

            dis = tem

        if dis[dst] == INF:
            return -1
        else:
            return dis[dst]

        