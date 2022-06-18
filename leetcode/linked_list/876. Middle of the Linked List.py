# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mptr = head
        eptr = head.next

        while eptr != None:
            eptr = eptr.next
            mptr = mptr.next

            if eptr is None:
                return mptr

            eptr = eptr.next

        return mptr 