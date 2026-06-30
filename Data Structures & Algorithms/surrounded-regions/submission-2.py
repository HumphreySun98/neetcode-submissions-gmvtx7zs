class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        queue = deque()


        for i in range(rows):
            if board[i][0] == 'O':
                board[i][0] = 'T'
                queue.append((i,0))
        for i in range(rows):
            if board[i][cols-1] == 'O':
                board[i][cols-1] = 'T'
                queue.append((i,cols-1))
        for i in range(cols):
            if board[0][i] == 'O':
                board[0][i] = 'T'
                queue.append((0,i))
        for i in range(cols):
            if board[rows-1][i] == 'O':
                board[rows-1][i] = 'T'
                queue.append((rows-1,i))


        


        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:

            r,c = queue.popleft()

            for dr, dc in directions:
                nr,nc = r+dr, c +dc


                if (0<= nr < rows and 0<=nc<cols and board[nr][nc] == 'O'):
                    board[nr][nc] = 'T'
                    queue.append((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                elif board[i][j] == 'T':
                    board[i][j] = 'O'
                





        