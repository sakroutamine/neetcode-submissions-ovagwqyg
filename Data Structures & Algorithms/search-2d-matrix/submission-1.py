class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])-1
        ly,ry = 0,len(matrix)-1
        var = 0
        my = 0
        while ly<=ry:
            my = (ry+ly) //2
            if matrix[my][0] > target:
                ry = my-1
            elif matrix[my][-1] < target:
                ly = my+1
            else:
                break
        
        while l<=r:
            m = (r+l) //2
            if matrix[my][m] > target:
                r = m-1
            elif matrix[my][m] < target:
                l = m+1
            elif matrix[my][m] == target:
                return True
        
        return False