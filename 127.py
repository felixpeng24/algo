"""
Easy

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linked_list_to_number(head):
    num = 0
    multiplier = 1
    while head:
        num += head.val * multiplier
        multiplier *= 10
        head = head.next
    return num

def number_to_linked_list(num):
    dummy = ListNode()
    current = dummy
    for digit in str(num)[::-1]:  # Reverse iteration
        current.next = ListNode(int(digit))
        current = current.next
    return dummy.next

def add_linked_lists(l1, l2):
    num1 = linked_list_to_number(l1)
    num2 = linked_list_to_number(l2)
    total = num1 + num2
    return number_to_linked_list(total)




def num_to_linked(num):
    dummy = ListNode()
    curr = dummy
    for digit in str(num)[::-1]:
        curr.next = ListNode(int(digit))
        curr = curr.next
    return dummy.next

