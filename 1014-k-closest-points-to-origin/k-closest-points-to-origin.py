class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            # d^2 = x^2 + y^2
            d = point[0]**2 +point[1]**2
            heapq.heappush(maxHeap, [-d,point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for _,point in maxHeap]
        
        