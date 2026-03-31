"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        l = 0
        r=0
        maxi = 0
        curr = 0
        while l < len(end):
            if start[l] < end[r]:
                l+=1
                curr+=1
            else:
                r+=1
                curr-=1
            maxi = max(curr,maxi)
        return maxi
