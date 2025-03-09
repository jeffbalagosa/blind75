from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head


class TestRemoveNthFromEnd(unittest.TestCase):
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

    def test_single_node(self):
        head = self.create_linked_list([1])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [])

    def test_two_nodes_remove_last(self):
        head = self.create_linked_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 1)
        self.assertEqual(self.linked_list_to_list(result), [1])

    def test_two_nodes_remove_first(self):
        head = self.create_linked_list([1, 2])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [2])

    def test_three_nodes_remove_middle(self):
        head = self.create_linked_list([1, 2, 3])
        result = self.solution.removeNthFromEnd(head, 2)
        self.assertEqual(self.linked_list_to_list(result), [1, 3])

    def test_five_nodes_remove_third_from_end(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(head, 3)
        self.assertEqual(self.linked_list_to_list(result), [1, 2, 4, 5])


if __name__ == "__main__":
    unittest.main()
