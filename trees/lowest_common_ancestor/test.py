import unittest
from trees.TreeNode.tree_node import TreeNode
from trees.lowest_common_ancestor.problem import Solution


class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lca(self):
        # Create the tree
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        # Test cases
        p = root.left  # Node with value 2
        q = root.right  # Node with value 8
        self.assertEqual(self.solution.lowestCommonAncestor(root, p, q), root)

        p = root.left  # Node with value 2
        q = root.left.right  # Node with value 4
        self.assertEqual(self.solution.lowestCommonAncestor(root, p, q), root.left)

        p = root.left.right.left  # Node with value 3
        q = root.left.right.right  # Node with value 5
        self.assertEqual(
            self.solution.lowestCommonAncestor(root, p, q), root.left.right
        )


if __name__ == "__main__":
    unittest.main()
