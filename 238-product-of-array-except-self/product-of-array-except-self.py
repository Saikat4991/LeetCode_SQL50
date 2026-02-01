class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = []
        postProduct = []
        preTemp = 1
        postTemp = 1

        for i in range(len(nums)):
            preProduct.append(preTemp)
            preTemp = preTemp*nums[i]

            postProduct.append(postTemp)
            postTemp= postTemp * nums[len(nums)-1 -i]

        result = []
        for i in range(len(nums)):
            result.append(preProduct[i]*postProduct[len(nums)-1 -i])

        return result

