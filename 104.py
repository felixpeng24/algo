"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""

# normally two pointers to check for palindrome
# what if we used stack?

stack = [] # issue is space complexity
#can you get length of linkedlist? or what if we just added everything onto a list instead and just two pointer method it

# if doubly linked, can use two pointer method using next and prev function

# singly linked:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

def linkedpalindrome(head):
    if not head or not head.next:
        return True
    
    #make a pointer at the center of the linked list

    slow = fast = head
    while fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    curr = slow
    while curr.next:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    left = head
    right = prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    
    return True

# lets try recursively rveersing linkedlist:

def reverse(head):
    if not head.next:
        return head
    recurseHead = reverse(head.next)
    head.next.next = head
    head.next = None
    return recurseHead

#Updating email for commits