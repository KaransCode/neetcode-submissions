class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        count = 0
        sorted_dict = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))
        
        for key, value in sorted_dict.items():
            if count == k:
                break
            res.append(key)
            count += 1
        res = sorted(res)
        return res
        