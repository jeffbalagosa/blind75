# Invert Binary Tree

## Level: Easy

## Description

You are given the root of a binary tree `root`. Your task is to invert the binary tree and return its root. Inverting a binary tree involves swapping the left and right children of all nodes in the tree.

---

### Example 1:

**Input:**
`root = [1, 2, 3, 4, 5, 6, 7]`

**Output:**
`[1, 3, 2, 7, 6, 5, 4]`

**Explanation:**
The input tree:
```
      1
     / \
    2   3
   / \ / \
  4  5 6  7
```

After inversion:
```
      1
     / \
    3   2
   / \ / \
  7  6 5  4
```

---

### Example 2:

**Input:**
`root = [3, 2, 1]`

**Output:**
`[3, 1, 2]`

**Explanation:**
The input tree:
```
    3
   / \
  2   1
```

After inversion:
```
    3
   / \
  1   2
```

---

### Example 3:

**Input:**
`root = []`

**Output:**
`[]`

**Explanation:**
An empty tree remains empty after inversion.

---

## Constraints:

- `0 <= The number of nodes in the tree <= 100`
- `-100 <= Node.val <= 100`

---

## Hints:

1. The left and right children of every node in the tree are swapped. Can you think of a way to achieve this recursively?
2. You can use the **Depth First Search (DFS)** algorithm:
   - At each node, swap its left and right children by exchanging their pointers.
   - Recursively visit the left and right children to perform the same operation.
   - If the current node is `null`, simply return.

---

## Recommended Complexity:

- **Time Complexity:** `O(n)`, where `n` is the number of nodes in the tree.
- **Space Complexity:** `O(n)`, to account for the recursion stack in the worst case (tree is completely unbalanced).
