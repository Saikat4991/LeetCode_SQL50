class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # value: index

        for i, x in enumerate(nums):
            diff = target - x
            if diff in prevMap:
                return [ prevMap[diff], i]
            prevMap[x] = i

        return
