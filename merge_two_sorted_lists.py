"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(0)
        while list1 != None and list2!= None:
            if list1.val < list2.val:
                obj = ListNode(list1.val)
                temp.next = obj
                list1 = list1.next
            else:
                obj = ListNode(list2.val)
                temp.next = obj
                list2 = list2.next
        temp.next = list1 or list2
        return dummy.next

