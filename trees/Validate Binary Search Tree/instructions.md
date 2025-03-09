# 98. Validate Binary Search Tree

**Difficulty:** Medium

## Problem Statement

Given the `root` of a binary tree, determine if it is a **valid binary search tree (BST)**.

A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be **binary search trees**.

---

## Example 1:

**Input:**
```plaintext
root = [2,1,3]
```
**Output:**
```plaintext
true
```

**Explanation:**
The tree structure is:
```
    2
   / \
  1   3
```
This satisfies the BST properties.

---

## Example 2:

**Input:**
```plaintext
root = [5,1,4,null,null,3,6]
```
**Output:**
```plaintext
false
```

**Explanation:**
The tree structure is:
```
    5
   / \
  1   4
     / \
    3   6
```
Here, the node with value `4` violates the BST rule because it is in the right subtree of `5` but has a left child `3`, which is **less than** `5`.

---

## Constraints:

- The number of nodes in the tree is in the range **`[1, 10⁴]`**.
- **`-2³¹ ≤ Node.val ≤ 2³¹ - 1`**.

---

## Related Topics

- [Tree](https://leetcode.com/tag/tree/)
- [Depth-First Search](https://leetcode.com/tag/depth-first-search/)
- [Binary Search Tree](https://leetcode.com/tag/binary-search-tree/)
- [Binary Tree](https://leetcode.com/tag/binary-tree/)
