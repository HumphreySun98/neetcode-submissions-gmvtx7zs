class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(1,0),(0,1)]
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if r == m-1 and c  == n-1:
                return 1

            count = 0
            for dr , dc in directions:
                nr, nc = r+dr, c+dc
                

                if 0<= nr < m and 0 <= nc < n:
                    count += dfs(nr,nc)
                    memo[(nr,nc)] = dfs(nr,nc)


            memo[(r,c)] = count


            return count


        return dfs(0,0)
                

        