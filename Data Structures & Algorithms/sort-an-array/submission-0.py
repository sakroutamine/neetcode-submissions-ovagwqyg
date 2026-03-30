class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeHelper(arr,L,M,R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            
            i, j, k = L,0,0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j < len(left):
                arr[i] = left[j]
                i+=1 
                j +=1
            while  k < len(right):
                arr[i] = right[k]
                i+=1 
                k+=1 
            
            return arr

             
        def mergeSort(arr, l, r):
            if l==r:
                return arr

            m=(l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            mergeHelper(arr,l,m,r)
            return arr

        return mergeSort(nums, 0, len(nums)-1)






    # def sorter(self, l, r, nums) ->List[int]:
    #     while l<r:
    #         m=(l+r)//2
    #         while nums[l] < nums[m]:
    #             l+=1
    #         while nums[m] < nums[r]:
    #             r-=1
    #         if l <= r:
    #             nums[l], nums[r] = nums[r], nums[l]
    #             l+=1
    #             r-=1
    #     return nums
    # def sortArray(self, nums: List[int]) -> List[int]:
    #     nums=self.sorter(0,len(nums)-1,nums)
    #     return nums
            
