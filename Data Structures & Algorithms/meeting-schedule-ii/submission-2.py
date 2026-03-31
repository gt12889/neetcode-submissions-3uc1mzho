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
        maxi = 0
        curr,l,r =0,0,0
        while l< len(start):
            if start[l] < end[r]:
                l+=1
                curr+=1
            else:
                curr-=1
                r+=1
            maxi =max(maxi,curr)
        return maxi
