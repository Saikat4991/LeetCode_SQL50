class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            start = 0
            end = col-1
            while start <= end:
                mid = start + (end-start)//2
                if target> matrix[i][mid]:
                    start = mid+1
                elif target<matrix[i][mid]:
                    end=mid-1
                else:
                    return True
        return False
        