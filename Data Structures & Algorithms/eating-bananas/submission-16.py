class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<r:
            sums=0
            m=(r+l)//2
            for i in piles:
                sums+=math.ceil(i/m)
            if sums<=h:
                r=m
            else:
                l=m+1
        return l

            

