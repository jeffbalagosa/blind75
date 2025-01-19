# Leetcode Problem: 235. Lowest Common Ancestor of a Binary Search Tree

## Difficulty: Medium

## Description
Given a binary search tree (BST), a tree structure in which each node has a value greater than all nodes in its left subtree and less than all nodes in its right subtree, find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor):

“The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

---

## Example 1:
**Input**:
```
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
```
**Output**:
```
6
```
**Explanation**: The LCA of nodes 2 and 8 is 6, as it is the lowest node in the BST that has both 2 in its left subtree and 8 in its right subtree.

---

## Example 2:
**Input**:
```
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
```
**Output**:
```
2
```
**Explanation**: The LCA of nodes 2 and 4 is 2, as it is the lowest node in the BST that has both 2 and 4 as descendants. Node 2 is also a direct ancestor of node 4, which makes it the LCA.

---

## Example 3:
**Input**:
```
root = [2,1], p = 2, q = 1
```
**Output**:
```
2
```

---

## Constraints:
1. The number of nodes in the tree is in the range `[2, 10^5]`, which necessitates an efficient algorithm to handle potentially large inputs within a reasonable timeframe.
2. `-10^9 <= Node.val <= 10^9`
3. All `Node.val` are **unique**.
4. `p != q`
5. `p` and `q` will exist in the BST, which simplifies the problem as it guarantees that both nodes are valid and present in the tree, allowing the solution to focus solely on finding their LCA without additional checks for their existence.
