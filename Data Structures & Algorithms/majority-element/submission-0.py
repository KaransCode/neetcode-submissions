class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate1 = 0
        count = 0

        for num in nums:

            if count == 0:
                candidate1 = num
                count += 1
            elif num == candidate1:
                count += 1
            else:
                count -= 1
        return candidate1