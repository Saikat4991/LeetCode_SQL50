class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marged = nums1+nums2
        marged.sort()
        n = len(marged)
        if n%2 == 0:
            return (marged[n//2 -1] + marged[n//2])/2.0
        else:
            return marged[n//2]