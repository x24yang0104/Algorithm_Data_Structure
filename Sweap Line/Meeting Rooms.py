"""
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
(0,8),(8,10) is not conflict at 8
Example1
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict

Example2
Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
"""

"""
Solution: Sort and loop
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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda x: (x.start, x.end))
        last_end = -1
        for interval in intervals:
            if interval.start < last_end:
                return False
            last_end = interval.end
        return True
"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

"""
Solution 2: Sweap Line, prefix sum version. 
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
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        if not intervals:
            return True
        max_val = float('-inf')
        for interval in intervals:
            max_val = max(max_val, interval.start)
            max_val = max(max_val, interval.end)

        count = [0 for _ in range(max_val + 1)]
        for interval in intervals:
            count[interval.start] += 1
            count[interval.end] -= 1
        
        total = 0
        for x in count:
            total += x
            if total > 1:
                return False
        return True
"""
Time Complexiy: O(n)
Space Complexity: O(n)
"""




        