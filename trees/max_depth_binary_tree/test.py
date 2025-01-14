import unittest
from problem import Solution
from trees.TreeNode.tree_node import TreeNode

class TestMaxDepthBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_two_level_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_three_level_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 4)

if __name__ == '__main__':
    unittest.main()
