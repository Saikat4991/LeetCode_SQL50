class Solution:
    def smallerToLeft_index(self, nums: List[int]) -> int:
        idx = []
        stack = [] #[values,index]
        n = len(nums)
        psudoIndex = -1
        for i in range(n):
            if not stack:
                idx.append(psudoIndex)
            elif stack and stack[-1][0] < nums[i]:
                idx.append(stack[-1][1])
            elif stack and stack[-1][0]>= nums[i]:
                while stack and stack[-1][0] >= nums[i]:
                    stack.pop()
                if not stack:
                    idx.append(psudoIndex)
                else:
                    idx.append(stack[-1][1])
            stack.append([nums[i],i])
 
        return idx

    def smallerToRight_index(self, nums: List[int]) -> int:
        idx = []
        stack = [] #[values,index]
        n = len(nums)
        psudoIndex = n
        for i in range(n-1,-1,-1):
            if not stack:
                idx.append(psudoIndex)
            elif stack and stack[-1][0] < nums[i]:
                idx.append(stack[-1][1])
            elif stack and stack[-1][0]>= nums[i]:
                while stack and stack[-1][0] >= nums[i]:
                    stack.pop()
                if not stack:
                    idx.append(psudoIndex)
                else:
                    idx.append(stack[-1][1])
            stack.append([nums[i],i])
        return idx[::-1]
                


    def largestRectangleArea(self, heights: List[int]) -> int:
        STL_Idx = self.smallerToLeft_index(heights)
        STR_Idx = self.smallerToRight_index(heights)
        maxArea = 0
        for i in range(len(heights)):
            width = (STR_Idx[i]-STL_Idx[i]) -1
            maxArea = max(maxArea, heights[i]*width)
        return maxArea
        
        