class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        mergedInterval = []
        intervals.append(newInterval)
        intervals.sort()
        for interval in intervals:

            if not mergedInterval or mergedInterval[-1][1] < interval[0]:
                mergedInterval.append(interval)
            else:
                mergedInterval[-1][1] = max(mergedInterval[-1][1], interval[1])
        return mergedInterval
        