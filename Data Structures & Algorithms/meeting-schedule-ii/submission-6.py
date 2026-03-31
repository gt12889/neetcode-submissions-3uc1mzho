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
        count = 0
        j=0
        i=0
        room =0
        while i < len(end):
            if start[i] < end[j]:
                room+=1
                i+=1
            else:
                room-=1
                j+=1
            count = max(count,room)
        return count
                