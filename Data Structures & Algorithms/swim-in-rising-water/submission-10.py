class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0],0,0)]
        dist = [[float('inf')] * n for _ in range(n)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        dist[0][0] = grid[0][0]
        
        while min_heap:
            time,r,c = heapq.heappop(min_heap)
            if time > dist[r][c]:
                continue

            if r  == n-1 and c == n-1:
                return time

            for dr,dc in directions:
                nr,nc =r+dr,c+dc
                if 0<=nr<n and 0<=nc<n:
                    next_time = max(time,grid[nr][nc])
                    if next_time < dist[nr][nc]:
                        dist[nr][nc] = next_time
                        heapq.heappush(min_heap,(dist[nr][nc],nr,nc))

        return -1
        