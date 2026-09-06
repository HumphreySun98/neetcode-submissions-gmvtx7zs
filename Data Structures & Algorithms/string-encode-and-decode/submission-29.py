class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            n =len(i)
            m = str(n)

            res += m + '#' + i

        return res



    def decode(self, s: str) -> List[str]:
        res = []

        i = 0 
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = s[i:j]
            length = int(l)
            res.append(s[j+1:j+1+length])
            i = j+1+length


        return res
