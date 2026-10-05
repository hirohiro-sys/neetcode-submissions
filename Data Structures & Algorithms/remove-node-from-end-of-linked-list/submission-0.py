# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

       # leftとrightにN+1の差分を作っておくことで、次のwhileで同時に2つを動かした際、最終的にleftが削除対象の値になる
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
        