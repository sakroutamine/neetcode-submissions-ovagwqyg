class Solution:

    def __init__(self, w: List[int]):
        self.arr = [0]
        self.sums = 0
        i = 0
        for j in w:
            i=i+j
            self.arr.append(i)
        self.sums = i
        print(self.sums, self.arr)

    def pickIndex(self) -> int:
        rand = random.uniform(0, self.sums)
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