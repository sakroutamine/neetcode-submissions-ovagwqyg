class Solution:

    def __init__(self, w: List[int]):
        self.arr = [0]
        for i in w:
            self.arr.append(self.arr[-1]+i)

    def pickIndex(self) -> int:
        rand = random.uniform(0, self.arr[-1])
        l,r = 0,len(self.arr)-1
        while l<r:
            m=(l+r)//2
            if rand > self.arr[m]:
                l=m+1
            elif rand < self.arr[m]:
                r=m
            
            print(l,r)
        return l-1




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()