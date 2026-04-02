class Solution:

    def __init__(self, w: List[int]):
        self.weighted = []
        self.tot = 0
        for i in range(len(w)):
            self.tot+=w[i]
            self.weighted.append(self.tot)
        
        print(self.weighted)

    def pickIndex(self) -> int:
        rand = random.randint(0,self.tot)
        l,r = 0, len(self.weighted)-1
        print(self.weighted, self.tot, rand)
        while l<r:
            m=(l+r)//2
            if self.weighted[m] > rand:
                r=m
            elif self.weighted[m] <= rand:
                l=m+1
            
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()