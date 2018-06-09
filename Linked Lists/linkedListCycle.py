# LeetCode

# @param head : Head node of linked list
# @return boolean. True if linked list has a cycle else return False

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        fastPointer = head
        slowPointer = head
        while fastPointer != None and fastPointer.next != None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                return True
        return False
