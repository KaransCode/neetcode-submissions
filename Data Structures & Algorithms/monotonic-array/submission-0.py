class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        monotoneIncreasing = 0
        monotoneDecreasing = 0

        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                monotoneIncreasing += 1

            if  nums[i] >= nums[i+1]:
                monotoneDecreasing += 1

        if (n-1) == monotoneIncreasing or (n-1) == monotoneDecreasing:
            return True 
        else:
            return False
