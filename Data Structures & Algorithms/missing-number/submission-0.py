class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = (n * (n+1))//2
        actualSum = sum(nums)
        return totalSum - actualSum