class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        inserted = False
        for interval in intervals:
            if not inserted and newInterval[0] < interval[0]:
                res.append(newInterval)
                inserted = True
            
            res.append(interval)
            
        if not inserted:
            res.append(newInterval)
            
        mergedInterval = []
        for interval in res:
            if not mergedInterval or mergedInterval[-1][1] < interval[0]:
                mergedInterval.append(interval)
            else:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], interval[1])
        return mergedInterval