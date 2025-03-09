# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium

## Problem Statement

Given the `root` of a binary tree, return the **level order traversal** of its nodes' values. (i.e., from left to right, level by level).

---

## Example 1:

**Input:**
```plaintext
root = [3,9,20,null,null,15,7]
```
**Output:**
```plaintext
[[3],[9,20],[15,7]]
```

**Explanation:**
The tree structure is:
```
      3
     / \
    9  20
      /  \
     15   7
```
Traversing level by level:
```
[
  [3],
  [9,20],
  [15,7]
]
```

---

## Example 2:

**Input:**
```plaintext
root = [1]
```
**Output:**
```plaintext
[[1]]
```

---

## Example 3:

**Input:**
```plaintext
root = []
```
**Output:**
```plaintext
[]
```

---

## Constraints:

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 ≤ Node.val ≤ 1000`.

---

## Related Topics

- [Tree](https://leetcode.com/tag/tree/)
- [Breadth-First Search](https://leetcode.com/tag/breadth-first-search/)
- [Binary Tree](https://leetcode.com/tag/binary-tree/)

---

## Hint:

- Use a queue to perform **Breadth-First Search (BFS)**.
