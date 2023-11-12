import unittest

from problem import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def test_is_subtree_true(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        solution = Solution()
        self.assertTrue(solution.isSubtree(root, subRoot))

    def test_is_subtree_false(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(0))
        solution = Solution()
        self.assertFalse(solution.isSubtree(root, subRoot))

    def test_both_none(self):
        solution = Solution()
        self.assertTrue(solution.isSubtree(None, None))

    def test_root_none(self):
        subRoot = TreeNode(1)
        solution = Solution()
        self.assertFalse(solution.isSubtree(None, subRoot))

    def test_subroot_none(self):
        root = TreeNode(1)
        solution = Solution()
        self.assertTrue(solution.isSubtree(root, None))

    def test_same_single_node(self):
        root = TreeNode(1)
        subRoot = TreeNode(1)
        solution = Solution()
        self.assertTrue(solution.isSubtree(root, subRoot))

    def test_root_single_node_subroot_multiple_nodes(self):
        root = TreeNode(1)
        subRoot = TreeNode(1, TreeNode(2))
        solution = Solution()
        self.assertFalse(solution.isSubtree(root, subRoot))


if __name__ == "__main__":
    unittest.main()
