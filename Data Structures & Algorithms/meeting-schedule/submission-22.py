"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        if not intervals:
            return True
        if len(intervals) ==1:
            return True

        for s in range(1,len(end)):
            if start[s] < end[s-1]:
                return False
        return True