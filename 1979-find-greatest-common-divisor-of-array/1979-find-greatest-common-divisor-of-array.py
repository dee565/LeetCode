class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        while maxNum != 0:
            minNum, maxNum = maxNum, minNum % maxNum
        return minNum        