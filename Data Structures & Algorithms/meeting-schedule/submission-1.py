"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start = sorted(start)
        end = sorted(end)

        for c in range(len(start)-1):
            if start[c+1] < end[c]:
                return False
        return True