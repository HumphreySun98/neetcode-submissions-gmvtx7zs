class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []


        for interval in intervals:
            s,e = interval


            if res and s <= res[-1][1]:
                res[-1][1] = max(res[-1][1],e)

            else:
                res.append(interval)


        return res
        