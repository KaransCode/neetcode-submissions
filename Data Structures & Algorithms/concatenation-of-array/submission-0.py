class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        limit = len(ans)
        for i in range(limit):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[(i+limit)%limit] = nums[i%n]
        return ans

        # return nums + nums  