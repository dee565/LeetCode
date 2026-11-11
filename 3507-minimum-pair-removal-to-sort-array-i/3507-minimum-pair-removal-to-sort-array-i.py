class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        while nums != sorted(nums):
            i = min(range(len(nums)-1),key=lambda x:nums[x]+nums[x+1])
            nums[i]+=nums[i+1]
            nums.pop(i+1)
            count+=1
        return count
        