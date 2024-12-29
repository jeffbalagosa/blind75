import unittest
from problem import Solution
from ..TreeNode.tree_node import TreeNode


def list_to_tree(lst):
    """
    Helper function to create a binary tree from a list.
    None values in the list represent null pointers.
    """
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        node = queue.pop(0)
        if node is None:
            continue
        node.left = TreeNode(lst[i]) if lst[i] is not None else None
        queue.append(node.left)
        if i + 1 < len(lst):
            node.right = TreeNode(lst[i + 1]) if lst[i + 1] is not None else None
            queue.append(node.right)
            i += 1
        i += 1
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_same_tree(self):
        tree1 = list_to_tree([1, 2, 3])
        tree2 = list_to_tree([1, 2, 3])
        self.assertTrue(self.sol.isSameTree(tree1, tree2))

    def test_different_tree(self):
        tree1 = list_to_tree([1, 2])
        tree2 = list_to_tree([1, None, 2])
        self.assertFalse(self.sol.isSameTree(tree1, tree2))

    def test_empty_tree(self):
        tree1 = list_to_tree([])
        tree2 = list_to_tree([])
        self.assertTrue(self.sol.isSameTree(tree1, tree2))


if __name__ == "__main__":
    unittest.main()
