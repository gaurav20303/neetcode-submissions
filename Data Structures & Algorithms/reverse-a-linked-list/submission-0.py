# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        curr = head
        while temp:
            curr = temp
            temp = curr.next
            if curr == head:
                curr.next = None
            else:
                curr.next = prev
            prev = curr
        return curr 
        