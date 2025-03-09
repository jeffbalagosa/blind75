from typing import List, Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next


class TestMergeKLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values):
        """Helper to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        """Helper to convert linked list back to a list for comparison."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_empty_input(self):
        result = self.solution.mergeKLists([])
        self.assertIsNone(result)

    def test_single_empty_list(self):
        result = self.solution.mergeKLists([None])
        self.assertIsNone(result)

    def test_single_list(self):
        lst = self.create_linked_list([1, 4, 5])
        result = self.solution.mergeKLists([lst])
        self.assertEqual(self.linked_list_to_list(result), [1, 4, 5])

    def test_two_lists(self):
        lst1 = self.create_linked_list([1, 4, 5])
        lst2 = self.create_linked_list([1, 3, 4])
        result = self.solution.mergeKLists([lst1, lst2])
        self.assertEqual(self.linked_list_to_list(result), [1, 1, 3, 4, 4, 5])

    def test_three_lists_with_empty(self):
        lst1 = self.create_linked_list([2, 6])
        lst2 = None
        lst3 = self.create_linked_list([1, 3, 5])
        result = self.solution.mergeKLists([lst1, lst2, lst3])
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 5, 6])

    def test_multiple_lists(self):
        lst1 = self.create_linked_list([1, 7])
        lst2 = self.create_linked_list([2, 4, 6])
        lst3 = self.create_linked_list([3, 5])
        result = self.solution.mergeKLists([lst1, lst2, lst3])
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
