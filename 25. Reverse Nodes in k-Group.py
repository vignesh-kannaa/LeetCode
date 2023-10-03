"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            kth = self.findKthNode(grpPrev, k)
            if not kth:  # breaking condition
                break

            # handle first section => connect first to grpnext
            grpNext = kth.next
            prev, cur = grpNext, grpPrev.next
            while cur != grpNext:  # have to update the kth element so swap till grpnext
                temp = cur.next
                prev, cur.next = cur, prev
                cur = temp

            # handle second section => connect last to grpprev
            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp
        return dummy.next

    def findKthNode(self, grpPrevious, k):
        cur = grpPrevious
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


"""
1)dummy node
2) get grpPrevious & grpNext
swap till kth node and update these 2 varibles 
remember the diagram
"""
