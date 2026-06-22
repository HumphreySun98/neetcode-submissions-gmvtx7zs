class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node  = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        
        
        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r,c,node):
            if (r<0 or r >= rows or c<0 or c>= cols):
                return
            ch = board[r][c]
            if ch == '#' or ch not in node.children:
                return

            node = node.children[ch]
            if node.word:
                res.append(node.word)
                node.word = None

            tmp =board[r][c]
            board[r][c] = '#'
            dfs(r+1,c,node)
            dfs(r,c+1,node)
            dfs(r-1,c,node)
            dfs(r,c-1,node)

            board[r][c] = tmp

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root)

        return res

            


            


        