import unittest

from problem import Solution, ListNode


class TestSolution(unittest.TestCase):
    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
        self.assertEqual(Solution().reverseList(head), expected)

    def test_2(self):
        head = ListNode(1, ListNode(2))
        expected = ListNode(2, ListNode(1))
        self.assertEqual(Solution().reverseList(head), expected)

    def test_3(self):
        head = ListNode(1)
        expected = ListNode(1)
        self.assertEqual(Solution().reverseList(head), expected)

    def test_4(self):
        head = ListNode()
        expected = ListNode()
        self.assertEqual(Solution().reverseList(head), expected)


if __name__ == "__main__":
    unittest.main()
