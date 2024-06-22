'''You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []'''

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next

        if not values:
            return None

        heapq.heapify(values)
        dummy = ListNode(0)
        curr = dummy
        
        while values:
            val = heapq.heappop(values)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next