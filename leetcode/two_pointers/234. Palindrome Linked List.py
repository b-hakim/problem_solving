# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return True
        # get middle
        # reverse to middle
        # check palindrom

        p1, p2 = head, head

        while p2.next is not None and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next

        isOdd = False

        if p2.next is None:
            isOdd = True

        middle = p1

        def revList(head):
            prev = None

            while head is not None:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp

            return prev

        # [2, 1] [1]
        # p1, p2, middle = 1, 1

        right_partition = middle.next
        middle.next = None

        rev_left = revList(head)

        # print(rev_left.val, rev_left.next.val, rev_left.next.next)
        # print(right_partition.val, right_partition.next.val, right_partition.next.next)

        p1 = rev_left
        p2 = right_partition

        if isOdd:
            p1 = p1.next

        while p1 is not None:
            if p1.val != p2.val:
                return False

            p1 = p1.next
            p2 = p2.next

        # left = revList(rev_left)
        # rev_left.next = right_partition

        return True



