class Solution:
    def reverse(self, x: int) -> int:
        new = abs(x)
        new = str(new)
        new = new[::-1]
        new = int(new)

        if x < 0:
            new *= -1

        if new >= 2**31-1 or new <= (-2)**31:
            new = 0


        return new