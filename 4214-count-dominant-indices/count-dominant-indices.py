class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        avg_list = []
        count = 1
        for i in range(n-1,-1,-1):
            s = s+nums[i]
            avg_list.append(s/count)
            count += 1
        res = 0
        for i in range(n):
            if nums[i] > avg_list[n-1-i]:
                res = res+1
            
        return res







        