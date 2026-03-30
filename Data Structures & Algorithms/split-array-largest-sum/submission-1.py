class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r = max(nums), sum(nums)
        minmax = r

        def isMax(mid):
            subarr = 1
            m=mid
            for i in nums:
                if m-i < 0:
                    subarr +=1
                    m=mid
                m=m-i
            return subarr

        while l<=r:
            mid=(l+r)//2
            numarr= isMax(mid)
            if numarr > k:
                l=mid+1
            else:
                minmax=mid
                r=mid-1
                

        return minmax
        



        # ls,rs = 0,0
        # 
        # while l<=r:
        #     m= (l+r)//2
        #     ls = sum(nums[0:m])
        #     print(nums[0:m])
        #     rs = sum(nums[m:len(nums)])
        #     print(nums[m:len(nums)])
        #     if rs == ls:
        #         return ls
        #     elif rs < ls:
        #         r=m-1
        #     else:
        #         l=m+1

        #     print(rs,ls)
        
        # return max(ls,rs)
        