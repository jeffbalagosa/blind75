# Solution Guide: Lowest Common Ancestor of a Binary Search Tree

## Problem Link
[Problem Link](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/)

---

## Description
Given a binary search tree (BST) where all node values are **unique**, and two nodes from the tree `p` and `q`, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes `p` and `q` is the lowest node in a tree `T` such that both `p` and `q` are descendants, including the case where the ancestor node is either `p` or `q` itself. The ancestor is allowed to be a descendant of itself.

---

## Example 1
**Input**:
```
root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
```
**Output**:
```
5
```

---

## Example 2
**Input**:
```
root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
```
**Output**:
```
3
```
**Explanation**: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

---

## Constraints
1. `2 <= The number of nodes in the tree <= 100`.
2. `-100 <= Node.val <= 100`
3. `p != q`
4. `p` and `q` will both exist in the BST.

---

## Recommended Time & Space Complexity
- **Time Complexity**: O(h), where `h` is the height of the tree.
- **Space Complexity**: O(h).

---

## Hints

### Hint 1
A Binary Search Tree (BST) is a tree in which the values of all nodes in the left subtree of a node are less than the node's value, and the values of all nodes in the right subtree are greater than the node's value. Additionally, every subtree of a BST must also satisfy this property. This property can be leveraged to find the LCA.

### Hint 2
You can use **recursion** to traverse the tree. During traversal, check conditions that indicate which subtree to traverse, based on the values of `p` and `q` relative to the current node's value.

### Hint 3
If nodes `p` and `q` are in different subtrees, a split occurs, making the current node the LCA. For example, if `p` is in the left subtree and `q` is in the right subtree (or vice versa), the current node acts as the junction point, ensuring both `p` and `q` have it as their common ancestor. If both nodes lie in the same subtree, continue traversing that subtree recursively.

### Hint 4
The LCA can also be one of the nodes, `p` or `q`, if the current node matches either of them. When encountering one of the nodes during traversal, that node is the LCA.

---

## Approaches

### 1. Recursion

#### Algorithm:
- Traverse the BST recursively.
- If both `p` and `q` are smaller than the current node's value, the LCA lies in the left subtree. This is because, in a BST, all nodes in the left subtree of a node have values less than the node itself, ensuring that both `p` and `q` must be in the left subtree if their values are smaller.
- If both `p` and `q` are greater than the current node's value, the LCA lies in the right subtree.
- If one node is on the left and the other is on the right, or the current node matches one of `p` or `q`, the current node is the LCA.

#### Python Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # This function finds the lowest common ancestor of two nodes in a BST.
    # Input: root (TreeNode), p (TreeNode), q (TreeNode)
    # Output: TreeNode representing the LCA
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
```

#### Time & Space Complexity
- **Time Complexity**: O(h), where `h` is the height of the BST. This is because the algorithm traverses the tree from the root to the LCA, which can span at most the height of the tree.
- **Space Complexity**: O(h) for the recursion stack.

---

### 2. Iteration

#### Algorithm:
- Start from the root node and traverse iteratively.
- If both `p` and `q` are greater than the current node's value, move to the right subtree.
- If both `p` and `q` are smaller than the current node's value, move to the left subtree.
- If one is on the left and the other is on the right, or the current node matches one of `p` or `q`, the current node is the LCA.

#### Python Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
```

#### Time & Space Complexity
- **Time Complexity**: O(h) where `h` is the height of the BST.
- **Space Complexity**: O(1) for the iterative approach.
