"""
Given a linked list of numbers and a pivot k, partition the linked list 
so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3,
 the solution could be 1 -> 0 -> 5 -> 8 -> 3

"""

#iterate through the list

#extra space method: just store values where it is greater in an array, build linkedlist from that and remove from the original linkedlist

#in place??? we can reverse a linked list

class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next
    
def LLpartition(head, k):
    underK = ListNode()
    currUnder = underK
    dummy = ListNode()
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.value < k:
            currUnder.next = curr.next
            currUnder = currUnder.next
            curr.next = curr.next.next        
        else:
            curr = curr.next
    
    currUnder.next = dummy.next
    return underK.next

def LLpartitionpass(head, k):
    final = finalcurr = ListNode()
    dummy = ListNode()
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.val < k:
            finalcurr.next = curr.next
            finalcurr = finalcurr.next
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    finalcurr.next = dummy.next
    
    return final.next

def Linkedlist(head):
    res = []
    while head.next:
        res.append(head.val)
        head = head.next
    
    res.append(head.val)
    return res

def combine(nums, k):
    return Linkedlist(LLpartitionpass(listLinked(nums), k))



# turn a list into linkedlist:

# def list_to_linked(nums):
#     dummy = ListNode()
#     dummy.next = nums[0]
#     linked = dummy.next
#     head = dummy.next
#     for num in nums[1:]:
#         linked.next.value = nums
#         linked = linked.next
#     return head

def listLinked(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def popLinkedList(node, k):
    # pops value K from a linkedlist
    # l, r = node, node.next
    # while l.value == k and node.next:
    #     l = l.next
    #     r = r.next
    # while r.next:
    #     while r.value == k:
    #         r = r.next
    #         l.next = r
    
    # return l

    dummy = ListNode()
    dummy.next = node
    curr = dummy
    while curr.next:
        if curr.next.value == k:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next



# nums = [1, 4, 5, 8, 3, 2, 1]
nums = [2, 1, 4]
k = 3
print(combine(nums, k))