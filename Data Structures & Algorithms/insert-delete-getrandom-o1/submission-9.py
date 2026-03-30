import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.dic = defaultdict(int)


    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.arr.append(val)
        self.dic[val]=len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        print(self.arr, val)
        if val in self.dic and len(self.arr) > 0:
            index = self.dic.pop(val, -1)
            print(index)
            self.arr[index]=self.arr[-1]
            self.dic[self.arr[index]] = index
            self.arr.pop(-1)
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()