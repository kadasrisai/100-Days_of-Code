'''You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3] '''

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        current = head
        p1 = head
        p2 = head
        values = []
        while p2:
            values.append(p2.val)
            p2 = p2.next
        left, right = 0, len(values) - 1
        
        while left <= right:
            p1.val = values[left]
            p1 = p1.next
            if p1 is not None:
                p1.val = values[right]
                p1 = p1.next
            left += 1
            right -= 1
        