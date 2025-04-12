"""
Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

"""

# 12345  54321   345   12

#reverse linkedlist, then reverse first half second half?
#hard to reverse and do that, instead jsut make a loop with head and tail and break the tail somewhere


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: Compute the length
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Make the list circular
    tail.next = head

    # Step 3: Find the new tail (length - k % length - 1) and new head
    k = k % length
    steps_to_new_tail = length - k - 1
    new_tail = head
    for _ in range(steps_to_new_tail):
        new_tail = new_tail.next
    new_head = new_tail.next

    # Step 4: Break the cycle
    new_tail.next = None

    return new_head
