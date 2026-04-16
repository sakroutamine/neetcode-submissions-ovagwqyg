class Node():
    def __init__(self):
        self.end=False
        self.char={}
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.char:
                cur.char[c] = Node()
            cur = cur.char[c]
        cur.end=True
        return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = set()
        visit=set()
        root=Node()

        for i in words:
            root.addWord(i)

        rows,cols=len(board),len(board[0])

        def dfs(r,c,node,word):
            if (r<0 or c<0 or r==rows or c==cols or (r,c) in visit or board[r][c] not in node.char):
                return False
            visit.add((r,c))
            node=node.char[board[r][c]]
            word += board[r][c]

            if node.end:
                ret.add(word)

            
        
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word) 
            dfs(r, c+1, node, word) 
            dfs(r, c-1, node, word)  

            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(ret)

