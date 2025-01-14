# Leetcode Problem: 104. Maximum Depth of Binary Tree

## Difficulty: Easy

## Description
Given the `root` of a binary tree, return *its maximum depth*. Calculating the maximum depth is useful for understanding the structure of the tree, such as determining its balance or height.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node. The root node counts as the first level, and depth is measured by the number of levels in the tree.

---

## Example 1:
**Input**:
```
root = [3,9,20,null,null,15,7]
```
**Output**:
```
3
```
**Explanation**:
The tree has three levels: the root node (3), its children (9 and 20), and the leaf nodes (15 and 7).

---

## Example 2:
**Input**:
```
root = [1,null,2]
```
**Output**:
```
2
```
**Explanation**:
The tree has two levels: the root node (1) and its right child (2).

---

## Constraints:
1. The number of nodes in the tree is in the range `[0, 10^4]`. This ensures that the solution must handle large input sizes efficiently.
2. `-100 <= Node.val <= 100`. This constraint ensures that the node values are manageable and fit within typical integer ranges for computations.
