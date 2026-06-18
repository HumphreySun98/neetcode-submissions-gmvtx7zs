class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        path = []
        res = []
        board = [['.'] * n for _ in range(n) ] 

        def bt(row):
            if row == n:
                res.append([''.join(r) for r in board])
                return


            for col in range(n):
                if col in cols or (col - row) in diag1 or (col + row) in diag2:
                    continue
                
                cols.add(col)
                diag1.add(col-row)
                diag2.add(col+row)

                board[row][col] = 'Q'

                bt(row+1)
                cols.remove(col)
                diag1.remove(col-row)
                diag2.remove(col+row)
                board[row][col] = '.'


        bt(0)
        return res

