"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start = sorted(start)
        end = sorted(end)
        for i in range(1,len(end)):
            if start[i] < end[i-1]:
                return False
        return True