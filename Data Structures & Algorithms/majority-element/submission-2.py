class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums)//2]


















































        # nums.sort()
        # return (nums[(len(nums)-1)//2])