class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        output = []
        intervals.sort()
        j = 0
        n = len(intervals)
        for interval in intervals:
            
            # case where interval is just later than curr interval
            if newInterval[0] > interval[1]:
                output.append(interval)
            elif interval[0] > newInterval[1]:
                break
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            j += 1
        output.append(newInterval)
        if j < n:
            return output + intervals[j:]
        print(output)
        return output