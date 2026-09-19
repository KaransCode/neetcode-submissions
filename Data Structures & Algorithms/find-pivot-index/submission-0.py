class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [] 
        rightSum = []
        curr_sum = 0

        for num in nums:
            curr_sum += num
            leftSum.append(curr_sum)
        
        for num in nums:
            rightSum.append(curr_sum)
            curr_sum -= num
        
        for i in range(len(nums)):
            if rightSum[i] == leftSum[i]:
                return i
        return -1