from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    left_check = staticmethod(lambda val, limit: val < limit)
    right_check = staticmethod(lambda val, limit: val > limit)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.isValid(root.left, root.val, self.left_check) or not self.isValid(
            root.right, root.val, self.right_check
        ):
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValid(self, root: Optional[TreeNode], limit: int, check) -> bool:
        if not root:
            return True
        if not check(root.val, limit):
            return False
        return self.isValid(root.left, limit, check) and self.isValid(
            root.right, limit, check
        )


class TestIsValidBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values):
        """Helper to create a binary tree from a list (level-order)."""
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    def test_empty_tree(self):
        result = self.solution.isValidBST(None)
        self.assertTrue(result)

    def test_single_node(self):
        root = self.create_tree([1])
        result = self.solution.isValidBST(root)
        self.assertTrue(result)

    def test_valid_bst_two_levels(self):
        root = self.create_tree([2, 1, 3])
        result = self.solution.isValidBST(root)
        self.assertTrue(result)

    def test_valid_bst_three_levels(self):
        root = self.create_tree([5, 3, 7, 1, 4, 6, 8])
        result = self.solution.isValidBST(root)
        self.assertTrue(result)

    def test_invalid_bst_duplicate(self):
        root = self.create_tree([2, 2, 3])
        result = self.solution.isValidBST(root)
        self.assertFalse(result)

    def test_invalid_bst_right_violation(self):
        root = self.create_tree([5, 1, 4])
        result = self.solution.isValidBST(root)
        self.assertFalse(result)

    def test_invalid_bst_left_violation(self):
        root = self.create_tree([2, 3, 1])
        result = self.solution.isValidBST(root)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
