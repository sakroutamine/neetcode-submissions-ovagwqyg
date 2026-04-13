class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def iterToBox(i,j):
            jIndex = j//3
            iIndex = i//3
            return iIndex*3+jIndex

        for r in range(9): #rows
            
            for c in range(9): #cols
                
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])

                it = iterToBox(r,c)
                if board[r][c] in boxes[it]:
                    return False
                boxes[it].add(board[r][c])

        return True
                


