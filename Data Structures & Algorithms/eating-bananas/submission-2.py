class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)-1
        mit = r

        while l<=r:
            m = (l+r) //2
            sum = 0
            for i in piles:
                sum += math.ceil(i/ m)
                print(sum)
            if sum <= h:
                mit=min(sum,r)
                r = m-1
            elif sum > h:
                l = m+1
        return l

        