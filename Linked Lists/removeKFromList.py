# CodeFights

# Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.


# @param l : Head node of linked list
# @param k : integer to remove
# @return l without nodes with value == k

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l
