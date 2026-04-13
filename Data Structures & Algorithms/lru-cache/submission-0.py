class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value

        self.next = self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.cap = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prv = node.prev 
        nxt = node.next
        prv.next = nxt
        nxt.prev = prv


    def insert(self, node):
        nexthead = self.head.next
        self.head.next = node
        node.next = nexthead
        nexthead.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        print(self.dic.keys())
        if key in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = Node(key,value)
        self.insert(self.dic[key])

        if len(self.dic)>self.cap:
            
            del self.dic[self.tail.prev.key]
            self.remove(self.tail.prev)