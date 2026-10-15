from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  

        def TimeTakenToEateBananaPile(rate, piles):
            timeTaken = 0
            for pile in piles:
                timeTaken += ceil(pile/rate)
            return timeTaken
        
        low = 1
        high = max(piles)
        ans = high
        
        while low < high:
            rate = low + (high - low)//2
            totalhours = TimeTakenToEateBananaPile(rate, piles)
            
            if totalhours <= h:
                ans = rate
                high = rate
            else:
                low = rate + 1 
        return ans