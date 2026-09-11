# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0 ,None)
        cur=dummy
        point1 = list1
        point2 = list2
        while point1 and point2:
            if point1.val < point2.val:
                cur.next = point1
                point1 = point1.next
            else:
                cur.next = point2
                point2 = point2.next
            cur = cur.next
        while point1:
            cur.next = point1
            point1 = point1.next
            cur =cur.next
        while point2:
            cur.next = point2
            point2 = point2.next
            cur =cur.next

        return dummy.next
