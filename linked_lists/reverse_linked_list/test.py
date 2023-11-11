import unittest

from problem import Solution


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_linked_list(elements):
    dummy = ListNode(0)
    ptr = dummy
    for element in elements:
        ptr.next = ListNode(element)
        ptr = ptr.next
    return dummy.next


def linked_list_to_list(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse_empty_list(self):
        linked_list = list_to_linked_list([])
        reversed_list = self.solution.reverseList(linked_list)
        self.assertEqual(linked_list_to_list(reversed_list), [])

    def test_reverse_single_element_list(self):
        linked_list = list_to_linked_list([1])
        reversed_list = self.solution.reverseList(linked_list)
        self.assertEqual(linked_list_to_list(reversed_list), [1])

    def test_reverse_two_element_list(self):
        linked_list = list_to_linked_list([1, 2])
        reversed_list = self.solution.reverseList(linked_list)
        self.assertEqual(linked_list_to_list(reversed_list), [2, 1])

    def test_reverse_multiple_elements_list(self):
        linked_list = list_to_linked_list([1, 2, 3, 4, 5])
        reversed_list = self.solution.reverseList(linked_list)
        self.assertEqual(linked_list_to_list(reversed_list), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
