# Leetcode Problem: 104. Maximum Depth of Binary Tree

## Problem Link
[104. Maximum Depth of Binary Tree](https://neetcode.io/problems/depth-of-binary-tree/)

## Description
Given the `root` of a binary tree, return its **depth**.

The **depth** of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node. Calculating the depth helps determine the tree's structure, balance, and potential applications in algorithms.

---

## Examples

### Example 1
**Input**:
```
root = [1, 2, 3, null, null, 4]
```
**Output**:
```
3
```

### Example 2
**Input**:
```
root = []
```
**Output**:
```
0
```

---

## Constraints
1. The number of nodes in the tree is between 0 and 100, inclusive.
2. `-100 <= Node.val <= 100`

---

## Recommended Time & Space Complexity
- **Time Complexity**: `O(n)` where `n` is the number of nodes in the tree.
- **Space Complexity**: `O(n)`

---

## Hints

### Hint 1
From the definition of a binary tree's maximum depth, can you think of a way to achieve this recursively? Consider calculating the maximum depth of the subtrees before computing the depth at the root.

### Hint 2
Use the Depth First Search (DFS) algorithm to find the maximum depth of a binary tree, starting from the `root`. For each node, recursively calculate the maximum depth of its left and right subtrees and add one for the current node. Then return:
```
1 + max(leftDepth, rightDepth)
```
This ensures the maximum depth is correctly propagated up the recursion stack.

### Hint 3
The `+1` accounts for the current node's depth in the recursion. Pass the maximum depth from the current node's left and right subtrees to its parent to compute the longest path to a leaf node through this subtree.

---

## Approaches

### 1. Recursive DFS
This method uses recursion to compute the depth of the left and right subtrees and returns the maximum of the two, plus one for the current node.

**Python Implementation**:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

---

### 2. Iterative DFS (Stack)
This approach uses a stack to simulate the recursion process iteratively. It is particularly useful for avoiding recursion depth issues in Python.

**Python Implementation**:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
```

---

### 3. Breadth First Search
This method uses a queue to explore each level of the tree iteratively, keeping track of the depth level by level.

**Python Implementation**:
```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
```

---

## Time & Space Complexity

### Recursive DFS
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(h)`, where `h` is the height of the tree. This accounts for the recursion stack size.
  - **Best Case** (Balanced Tree): `O(log(n))`
  - **Worst Case** (Degenerate Tree): `O(n)`

### Iterative DFS (Stack)
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Breadth First Search
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`
