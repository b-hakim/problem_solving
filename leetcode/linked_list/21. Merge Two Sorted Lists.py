from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        out = None
        head = out

        while list1 != None:
            if out is None:
                out = ListNode()
                head = out
            else:
                out.next = ListNode()
                out = out.next

            if list2 == None:
                out.val = list1.val
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    out.val = list2.val
                    list2 = list2.next
                else:
                    out.val = list1.val
                    list1 = list1.next

        while list2 != None:
            if out is None:
                out = ListNode()
                head = out
            else:
                out.next = ListNode()
                out = out.next

            out.val = list2.val
            list2 = list2.next

        return head
