"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda time: time.start)
        prev = None
        for i in intervals:
            if prev is not None and i.start < prev.end:
                return False
            prev = i
        

        return True