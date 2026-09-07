class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                a = board[i][j]
                if a == '.':
                    continue



                box_index = (i // 3) *3 + (j//3)

                if a in row[i] or a in col[j] or a in box[box_index]:
                    return False


                row[i].add(a)
                col[j].add(a)
                box[box_index].add(a)





        return True
        