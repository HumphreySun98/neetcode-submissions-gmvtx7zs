class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def bt(left,right):
            if left == n and right == n:
                res.append("".join(path))

                return

            if left < n:
                path.append('(')
                bt(left+1,right)
                path.pop()


            if right < left:
                path.append(')')
                bt(left,right+1)


                path.pop()


        bt(0,0)
        return res


        