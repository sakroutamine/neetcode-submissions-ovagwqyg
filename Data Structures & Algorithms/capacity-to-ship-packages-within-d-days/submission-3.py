class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        ans = r

        while l<=r:
            mid=(l+r)//2
            sums=mid
            print(mid)
            day=1
            for i in weights:
                sums=sums-i
                if sums<0:
                    day+=1
                    sums=(l+r)//2 - i
            if day > days:
                print(day, l, r)
                l=mid+1
            else:
                ans=mid
                r=mid-1
            print(l,r)
        return ans
