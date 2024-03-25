"""
21. Merge Two Sorted Lists
--------------------------------------

Description:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.


Approach:
1. Initialize a new ListNode called merged which will serve as the dummy head of the merged list.
2. Initialize a temporary pointer called pointer pointing to the dummy head,
    this will keep track of the last node in merged.
3. Iterate through both linked lists simultaneously until one or both of them become empty:

    * Compare the values of the current nodes of both linked lists.
    * Attach the smaller node to pointer.next (add the smaller value to the merged linked list),
        and move the respective linked list pointer forward.
    * Move merged pointer forward (to go to the next node).

4. After the loop, if there are remaining nodes in either linked list,
    attach them to the end of the merged list.
5. Return the merged linked list, without the dummy head.\

Complexity:
Time complexity: O(m+n)
    * m and n are the length of the linked lists (list1 and list2)
Space complexity: O(1)

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        pointer = merged

        while list1 and list2:
            if list1.val < list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next

            pointer = pointer.next

        if list1:
            pointer.next = list1
        else:
            pointer.next = list2

        return merged.next


def print_solution(solution: ListNode):
    if solution is None:
        print("[]")
    else:
        while solution:
            print(solution.val)
            solution = solution.next


""" Example 1 """
# list1 = [1,2,4], list2 = [1,3,4]

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


solution1 = Solution().mergeTwoLists(list1, list2)
print("Solution 1: ")
print_solution(solution1)  # output -> [1,1,2,3,4,4]

""" Example 2 """
# list1 = [], list2 = []

list1 = None
list2 = None

solution2 = Solution().mergeTwoLists(list1, list2)
print("Solution 2: ")
print_solution(solution2)  # output -> []

""" Example 3 """
#  list1 = [], list2 = [0]

list1 = None
list2 = ListNode(0)

solution3 = Solution().mergeTwoLists(list1, list2)
print("Solution 3: ")
print_solution(solution3)  # output -> [0]
