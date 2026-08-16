class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        count = 0
        prev = float('-INF')


        for interval in intervals:
            s,e = interval
            if s >= prev:
                prev = e
                

            else:
                count += 1


        return count



        