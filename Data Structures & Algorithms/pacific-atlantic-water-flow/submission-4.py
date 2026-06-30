class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        res = []

        pa_q = deque()
        at_q = deque()
        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        for r in range(rows):
            pa_q.append((r,0))
            at_q.append((r,cols-1))
            pacific.add((r,0))
            atlantic.add((r,cols-1))

        for c in range(cols):
            pa_q.append((0,c))
            at_q.append((rows-1,c))
            pacific.add((0,c))
            atlantic.add((rows-1,c))


        while pa_q:
            r,c = pa_q.popleft()
            for dr,dc in directions:
                nr,nc =r+dr , c + dc

                if nr < 0 or nr >=rows or nc<0 or nc>=cols:
                    continue

                if (nr,nc) in pacific:
                    continue

                if  heights[nr][nc] < heights[r][c]:
                    continue

                
                pacific.add((nr,nc))

                pa_q.append((nr,nc))



        while at_q:
            r,c = at_q.popleft()
            for dr,dc in directions:
                nr,nc = r+ dr,c+dc

                if  nr < 0 or nr >=rows or nc<0 or nc>=cols:
                    continue


                if (nr,nc) in atlantic:
                    continue

                if heights[nr][nc] < heights[r][c]:
                    continue

                atlantic.add((nr,nc))
                at_q.append((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])


        return res




                



        