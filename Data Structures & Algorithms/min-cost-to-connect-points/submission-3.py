class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n 
        dist[0] = 0
        count = 0
        visited = [False] * n

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                     u = i

            visited[u] = True
            count += dist[u]


            for v in range(n):
                if not visited[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if d < dist[v]:                            
                        dist[v] = d


        return count




        