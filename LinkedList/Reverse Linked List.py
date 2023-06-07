"""
Description
Reverse a linked list.
The linked list length is less than 100

Example 1:
Input:
linked list = 1->2->3->null
Output:
3->2->1->null
Explanation:
Reverse Linked List

Example 2:
Input:
linked list = 1->2->3->4->null
Output:
4->3->2->1->null
Explanation:

Challenge
Reverse it in-place and in one-pass
"""
from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here
        if not head:
            return None
        next = head.next
        head.next = None
        while next:
            temp = next.next
            next.next = head
            head = next
            next = temp
        return head