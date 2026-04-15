class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        n=len(nums)-1
        nums.sort()

        for i in range(n-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k = i+1, n
            while j<k:

                zero = nums[i]+nums[j]+nums[k]
                if zero == 0:
                    ret.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1    
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif zero >0:
                    k-=1
                else:
                    j+=1

                
        return ret


