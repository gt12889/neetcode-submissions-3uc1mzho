"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start =[i.start for i in intervals]
        end = [i.end for i in intervals]
        start = sorted(start)
        end = sorted(end)
        cur = 0
        count = 0
        s,e = 0,0
        while s <= len(end)-1:
            if start[s] < end[e]:
                cur+=1 
                s+=1    
            else:
                if cur >0:
                    cur-=1
                e+=1
            count = max(count,cur)
        return count