class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []


        def bt(start,target):
            if target == 0:
                res.append(path[:])
                return

            if target < 0:
                return


            for i in range(start,len(nums)):
                path.append(nums[i])
                bt(i,target-nums[i])
                path.pop()

        
        bt(0,target)
        return res