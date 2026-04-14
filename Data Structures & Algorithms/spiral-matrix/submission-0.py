class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, top = 0,0
        r, bottom = len(matrix[0])-1, len(matrix)-1
        ret = []
        x, y=0,0
        while len(ret) < len(matrix)*len(matrix[0]):
            for x in range(l, r + 1):
                ret.append(matrix[y][x])
            top+=1
            
            print(x,y,l,r,top,bottom)
            for y in range(top, bottom + 1):
                ret.append(matrix[y][x])
            r-=1

            if not (l <= r and top <= bottom):
                break
            
            print(x,y,l,r,top,bottom)
            for x in range(r, l - 1, -1):
                ret.append(matrix[y][x])
            bottom-=1
            
            print(x,y,l,r,top,bottom)
            for y in range(bottom, top - 1, -1):
                ret.append(matrix[y][x])
            l +=1
            
            print(x,y,l,r,top,bottom)
        
        return ret
