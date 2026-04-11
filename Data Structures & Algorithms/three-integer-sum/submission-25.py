class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n = len(nums)-1
        nums=sorted(nums)
        print(nums)

        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=n
            while j<k:
                sums = nums[i]+nums[j]+nums[k]
                if sums==0:
                    ret.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif sums>0:
                    k-=1
                else:
                    j+=1
        return ret
