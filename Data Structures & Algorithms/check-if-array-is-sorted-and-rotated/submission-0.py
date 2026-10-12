class Solution:
    def check(self, nums: List[int]) -> bool:
        cut = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                cut += 1

        if cut <= 1:
            return True
        return False
        