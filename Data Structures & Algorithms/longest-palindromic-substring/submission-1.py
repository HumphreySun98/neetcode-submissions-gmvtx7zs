class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''

        def expand(r,l):
            while l>= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return s[l+1:r]


        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i+1,i)

            if len(odd) > len(res):
                res = odd

            if len(even) > len(res):
                res = even


        return res