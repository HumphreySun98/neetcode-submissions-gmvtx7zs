class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []


        def bt(start):
            if start == len(s):
                res.append(path[:])
                return 


            for end in range(start +1, len(s)+1):
                sub = s[start : end]

                if sub == sub[::-1]:
                    path.append(sub)
                    bt(end)
                    path.pop()

        bt(0)
        return res

            

            
        