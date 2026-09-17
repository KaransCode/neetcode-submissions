class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        print(type(seen))
        for num,value in enumerate(nums):
            difference = target - value
            if difference in seen:
                return [seen[difference],num]
            seen[value] = num