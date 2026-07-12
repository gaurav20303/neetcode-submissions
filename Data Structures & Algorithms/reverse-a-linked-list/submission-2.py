# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        curr = head.next
        prev.next = None

        while curr:
            print(curr.val)
            head = curr
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
            
            
        return head
            
        