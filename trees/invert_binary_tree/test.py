import unittest
from problem import TreeNode, Solution


def tree_to_list(root):
    """
    Helper function to convert a binary tree to a level-order list representation.
    """
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


def list_to_tree(values):
    """
    Helper function to create a binary tree from a level-order list representation.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestInvertBinaryTree(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        self.assertIsNone(self.solution.invertTree(None))

    def test_single_node_tree(self):
        root = TreeNode(1)
        inverted = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(inverted), [1])

    def test_two_level_tree(self):
        root = list_to_tree([1, 2, 3])
        inverted = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(inverted), [1, 3, 2])

    def test_three_level_tree(self):
        root = list_to_tree([1, 2, 3, 4, 5, 6, 7])
        inverted = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(inverted), [1, 3, 2, 7, 6, 5, 4])

    def test_tree_with_null_nodes(self):
        root = list_to_tree([1, 2, 3, None, 4, None, 5])
        inverted = self.solution.invertTree(root)
        self.assertEqual(tree_to_list(inverted), [1, 3, 2, 5, None, 4])

    def test_large_tree(self):
        root = list_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        inverted = self.solution.invertTree(root)
        self.assertEqual(
            tree_to_list(inverted), [1, 3, 2, 7, 6, 5, 4, 15, 14, 13, 12, 11, 10, 9, 8]
        )


if __name__ == "__main__":
    unittest.main()
