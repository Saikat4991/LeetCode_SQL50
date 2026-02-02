class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l,r = 0, len(height)-1
        while l<r:
            distance = (r-l)
            h = min(height[l],height[r])
            area = max(area, h*distance)

            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return area