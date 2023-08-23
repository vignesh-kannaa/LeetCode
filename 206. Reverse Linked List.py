"""Given the head of a singly linked list, reverse the list, and return the reversed list

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, cur = None, head
        # while cur:
        #   nxt = cur.next
        #   cur.next = prev
        #   prev = cur
        #   cur = nxt
        # return prev

        # RECURSIVE
        # base condition

        if not head:
            return None
        # recursive function
        nxthead = head
        if head.next:
            nxthead = self.reverseList(head.next)
            # B.next.next = B (which means C.next = B) This reverses the pointer between B and C:
            head.next.next = head
        head.next = None  # Finally, we set the current node's pointer to NULL:

        return nxthead
