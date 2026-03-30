class setList:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap: 

    def __init__(self):
        self.maps = [setList() for i in range(1000)]

    def hasher(self,key):
        return key % len(self.maps)

    def put(self, key: int, value: int) -> None:

        cur = self.maps[self.hasher(key)] 
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = setList(key, value)
        

    def get(self, key: int) -> int:
        cur = self.maps[self.hasher(key)] 
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.maps[self.hasher(key)] 
        while cur.next:
            if cur.next.key == key:
                val=cur.next.value
                cur.next = cur.next.next
                return 
            cur = cur.next
        return 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)