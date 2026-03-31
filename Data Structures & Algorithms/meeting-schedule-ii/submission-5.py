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
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        days=0
        d=0
        e,s=0,0
        if len(intervals) <=1:
            return 1
        while s < len(end):
            if start[s] < end[e]:
                s+=1
                d+=1
            else:
                d-=1
                e+=1
            days = max(days,d)
        return days




