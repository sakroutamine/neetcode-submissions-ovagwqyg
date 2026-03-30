class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        self.tot = sum(w)
        self.weg = [(i/(self.tot)) for i in w]
        for j in range(len(w)):
            for k in range(w[j]):
                self.arr.append(j)
        print(self.arr)

    def pickIndex(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()