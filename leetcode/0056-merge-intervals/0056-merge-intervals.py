class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        i = 0
        print(intervals)
        
        while(i<len(intervals)-1):
            if len(intervals) == 1:
                return intervals
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] <= intervals[i+1][1]:
                    intervals[i] = [intervals[i][0],intervals[i+1][1]]
                
                intervals.remove(intervals[i+1])
            else:
                i+=1
        return intervals