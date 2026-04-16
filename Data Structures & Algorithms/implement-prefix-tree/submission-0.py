class Node():
    def __init__(self):
        self.end=False
        self.children={}

class PrefixTree:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                newNode = Node()
                cur.children[c]=newNode
                cur=newNode
        cur.end=True
        return 


    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.end

    
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c in cur.children:
                cur=cur.children[c]
            else:
                return False
        return True
        