class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []


        phone = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        path = []
        res = []



        def bt(index):
            if index == len(digits):
                res.append(''.join(path))
                return


            letters = phone[digits[index]]
            for ch in letters:
                path.append(ch)
                bt(index + 1)
                path.pop()


        bt(0)
        return res
        