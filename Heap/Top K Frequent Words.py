"""
Description
Given a list of words and an integer k, return the top k frequent words in the list.
You should order the words by the frequency of them in the return list, the most frequent one comes first. If two words has the same frequency, the one with lower alphabetical order come first.

Example 1:
Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 3
Output: ["code", "lint", "baby"]

Example 2:
Input:
  [
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
  ]
  k = 4
Output: ["code", "lint", "baby", "yes"]

Challenge
Do it in O(nlogk) time and O(n) extra space.
"""

"""
Solution 1: quick select
"""
from typing import (
    List,
)
class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def top_k_frequent_words(self, words: List[str], k: int) -> List[str]:
        # write your code here
        if not words or k <= 0:
            return []
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        array = []
        for word, count in dict.items():
            array.append((-count, word))
        self.quickSelect(array, k - 1, 0, len(array) - 1)
        array = sorted(array[:k])
        result = []
        for word in array:
            result.append(word[1])
        return result
        
    def quickSelect(self, array, index, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = array[(left + right) // 2]
        while left <= right:
            while left <= right and (array[left][0] < pivot[0] or (array[left][0] == pivot[0] and array[left][1] < pivot[1])):
                left += 1
            while left <= right and (array[right][0] > pivot[0] or (array[right][0] == pivot[0] and array[right][1] > pivot[1])):
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        if index <= right:
            self.quickSelect(array, index, start, right)
        if index >= left:
            self.quickSelect(array, index, left, end)
        return
"""
Time Complexity: O(n + klogk)
Space Complexity: O(n)
"""

"""
Solution 2: HeapQ + self defined class. This question needs to sort the word by count desc first and then by dict order. So it is easier to implement a call and rewrite the __lt__ funciotn.
"""

from typing import (
    List,
)
import heapq

class Node:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count != other.count:
            return self.count < other.count
        return self.word > other.word


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def top_k_frequent_words(self, words: List[str], k: int) -> List[str]:
        # write your code here
        if not words or k <= 0:
            return []
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        queue = []
        for word, count in dict.items():
            heapq.heappush(queue, Node(count, word)) 
            if len(queue) > k:            
                heapq.heappop(queue)
        
        result = []
        while queue:
            result.append(heapq.heappop(queue).word)
        return result[::-1]


"""
Time Complexity: O(nlogk)
Space Complexity: O(n)
"""


















