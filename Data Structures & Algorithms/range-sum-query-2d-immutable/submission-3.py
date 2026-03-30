class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * (len(matrix[0])+1) for r in range(len(matrix)+1)]
        for r in range(len(matrix)):
            pre = 0
            for c in range(len(matrix[0])):
                pre += matrix[r][c]
                self.prefix[r+1][c+1] = pre + self.prefix[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = 0
        r1,c1, r2, c2 = row1+1, col1+1, row2+1,col2+1
        
        
        sums = self.prefix[r2][c2] - self.prefix[r1-1][c2] - self.prefix[r2][c1-1] + self.prefix[r1-1][c1-1]


        return sums

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)