"""
Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form.
 For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

 medium
"""

#create a new linkedlist
#append first two numbers if different
#move onto next number, if bigger, append on right, if smaller, append on left
#append to right and left based on linking the number to the head, or add to tail

#instead do in place swapping with a boolean
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def alternate_low_high(head):
    if not head or not head.next:
        return head

    current = head
    is_less = True  # Start with expecting current < next

    while current and current.next:
        if is_less:
            if current.val > current.next.val:
                current.val, current.next.val = current.next.val, current.val
        else:
            if current.val < current.next.val:
                current.val, current.next.val = current.next.val, current.val
        is_less = not is_less
        current = current.next

    return head
