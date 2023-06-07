"""
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)
(0,8),(8,10) is not conflict at 8

Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)

Example2
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
"""

"""
Solution: Sweap Line. Status version
"""
from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        times = []
        for interval in intervals:
            times.append((interval.start, True))
            times.append((interval.end, False))
        times.sort()
        meeting, rooms = 0, 0
        for time in times:
            if time[1]:
                meeting += 1
            else:
                meeting -= 1
            rooms = max(rooms, meeting)
        return rooms
    
"""
Time Complexity: O(nlogn)
Space complexity: O(n)
"""



