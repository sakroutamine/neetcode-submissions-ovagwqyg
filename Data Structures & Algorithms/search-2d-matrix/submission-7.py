class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        m=0
        lx,rx=0,len(matrix[0])-1
        while l<=r:
            m=(l+r)//2
            if matrix[m][0] > target:
                r=m-1
            elif matrix[m][-1] < target:
                l=m+1
            else:
                break
        
        while lx<=rx:
            mx=(lx+rx)//2
            if matrix[m][mx] == target:
                return True
            elif matrix[m][mx] > target:
                rx=mx-1
            else:
                lx=mx+1
        return False