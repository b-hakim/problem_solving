# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}

        while head is not None:
            if head in d:
                return head

            d[head] = True

            head = head.next

        return None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sptr, fptr = head, head

        if fptr is None:
            return None

        snode = None

        while fptr is not None:
            sptr = sptr.next
            fptr = fptr.next

            if fptr is None:
                return None

            fptr = fptr.next

            if fptr == sptr:
                snode = fptr
                break

        if fptr is None:
            return None

        sptr = head

        while sptr != fptr:
            sptr = sptr.next
            fptr = fptr.next

        return sptr
