from typing import List, Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


class TestLevelOrder(unittest.TestCase):
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
        result = self.solution.levelOrder(None)
        self.assertEqual(result, [])

    def test_single_node(self):
        root = self.create_tree([1])
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1]])

    def test_two_levels(self):
        root = self.create_tree([1, 2, 3])
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2, 3]])

    def test_three_levels_complete(self):
        root = self.create_tree([1, 2, 3, 4, 5, 6, 7])
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2, 3], [4, 5, 6, 7]])

    def test_three_levels_incomplete(self):
        root = self.create_tree([1, 2, 3, 4, None, 6])
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2, 3], [4, 6]])

    def test_left_skewed(self):
        root = self.create_tree([1, 2, None, 4])
        result = self.solution.levelOrder(root)
        self.assertEqual(result, [[1], [2], [4]])


if __name__ == "__main__":
    unittest.main()
