from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None


class TestReorderList(unittest.TestCase):
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

    def test_empty_list(self):
        head = None
        self.solution.reorderList(head)
        self.assertIsNone(head)

    def test_single_node(self):
        head = self.create_linked_list([1])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1])

    def test_two_nodes(self):
        head = self.create_linked_list([1, 2])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 2])

    def test_three_nodes(self):
        head = self.create_linked_list([1, 2, 3])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 3, 2])

    def test_four_nodes(self):
        head = self.create_linked_list([1, 2, 3, 4])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 4, 2, 3])

    def test_five_nodes(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.solution.reorderList(head)
        self.assertEqual(self.linked_list_to_list(head), [1, 5, 2, 4, 3])


if __name__ == "__main__":
    unittest.main()
