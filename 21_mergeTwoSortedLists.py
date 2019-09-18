"""
merge two sorted linked lists and return it as a new list.
The new list should be made splicing together the nodes of the first two lists

input 1 2 4, 1 3 4
output: 1 1 2 3 4 4
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoSortedLists(self, l1, l2):
        """

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        curr = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1.val
                l1 = l1.next
            else:
                curr.next = l2.val
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next


if __name__ == '__main__':

    s = Solution()
    print(s.mergeTwoSortedLists())