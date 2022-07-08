# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # idea: reverse node A,
        # last node in A (headA) will point to headB
        # if there is an intersection, then it will be at the start of the cycle
        # use floyd cycle algo to get the start of the cycle
        # break the cycle at headA
        # reverse the nodes
        # return A

        # listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]
        # revListA = [5, 4, 8, 1, 4]

        # prev = 5
        # t=None
        # tmp = None

        def revList(t):
            prev = None

            while t is not None:
                tmp = t.next
                t.next = prev
                prev = t
                t = tmp

            return prev

        reversed_list_a = revList(headA)

        headA.next = headB

        # now check for cycle
        t1, t2 = reversed_list_a, reversed_list_a

        while t2.next is not None and t2.next.next is not None:
            t1 = t1.next
            t2 = t2.next.next

            if t1 == t2:
                break

        if t2.next is None or t2.next.next is None:
            # no cycle
            # split at headA
            # reverse from reversed_list_a to headA
            headA.next = None
            revList(reversed_list_a)
            return None

        ## cycle is here
        # start from the beginning and from the intersection for t1, t2
        # inc one node at a time, until match
        # reverse A and return this node

        # [2,3-->2]
        #
        # t1, t2 = 3,3

        t1 = reversed_list_a
        # revListA = [5, 4, 8, 1, 4, 5, 6, 1 --> 8]
        # t1, t2 = 8, 8

        while t1 != t2:
            t1 = t1.next
            t2 = t2.next

        headA.next = None
        revList(reversed_list_a)

        return t1

# easier sol:
"""
Step 1-> Find the length of both linkedlists and take their difference 'd'
Step 2-> Move the larger node forward by 'd' steps
Step 3-> Now the starting point of both linkedlists are equidistant from intersection ,so move both pointers together untill the intersection is found.
TC->O(m+n) , SC->O(1)
"""