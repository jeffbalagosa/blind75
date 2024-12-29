### **226. Invert Binary Tree - Explanation**

---

#### **Problem Statement**
You are given the root of a binary tree, `root`. Your task is to **invert the binary tree** and return the modified root.

**[Problem Link](https://neetcode.io/problems/invert-a-binary-tree/)**

---

#### **How It Works (Step-by-Step)**

1. **Understanding Inversion**:
   - Inverting a binary tree involves swapping the left and right children of each node recursively or iteratively.
   - For example:
     ```
       Original Tree         Inverted Tree
            1                     1
           / \                   / \
          2   3                 3   2
         / \ / \               / \ / \
        4  5 6  7             7  6 5  4
     ```

2. **Approach**:
   - You can solve this problem using:
     - **Breadth First Search (BFS)**
     - **Depth First Search (DFS)** (Recursive or Iterative)
   - Each approach involves traversing the tree and swapping child nodes at each step.

---

#### **Examples**

1. **Example 1**
   - **Input**: `root = [1, 2, 3, 4, 5, 6, 7]`
   - **Output**: `root = [1, 3, 2, 7, 6, 5, 4]`

   ![Example 1 Image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/ac124ee6-207f-41f6-3aaa-dfb35815f200/public)

2. **Example 2**
   - **Input**: `root = [3, 2, 1]`
   - **Output**: `root = [3, 1, 2]`

   ![Example 2 Image](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e39e8d4f-9946-4f99-ee3d-0d4df08d4d00/public)

3. **Example 3**
   - **Input**: `root = []`
   - **Output**: `root = []`

---

#### **Constraints**
- \( 0 \leq \text{Number of nodes in the tree} \leq 100 \)
- \( -100 \leq \text{Node.val} \leq 100 \)

---

### **Hints for Solving**

1. **Understand the Swap**:
   - At each node, swap the left and right children.
   - Repeat this for all nodes in the tree.

2. **Recursive Solution**:
   - Use Depth First Search (DFS).
   - At each node:
     - Swap its left and right children.
     - Recursively apply this operation to its children.

3. **Iterative Solution**:
   - Use a queue or stack to process nodes one by one (BFS or DFS).
   - Swap the left and right children at each node.

---

#### **Time and Space Complexity**

- **Time Complexity**: \( O(n) \), where \( n \) is the number of nodes in the tree.
- **Space Complexity**: \( O(n) \), due to recursion stack or iterative traversal.

---

### **Solutions**

#### **1. Breadth First Search (BFS)**
This approach uses a queue to traverse the tree level-by-level.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])  # Start with the root node

        while queue:
            node = queue.popleft()  # Process the next node in the queue
            node.left, node.right = node.right, node.left  # Swap children

            if node.left:  # Add left child to the queue if it exists
                queue.append(node.left)
            if node.right:  # Add right child to the queue if it exists
                queue.append(node.right)

        return root  # Return the inverted tree
```

---

#### **2. Depth First Search (DFS) - Recursive**
This approach swaps the children of nodes using recursive calls.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None  # Base case: empty tree

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root  # Return the inverted tree
```

---

#### **3. Depth First Search (DFS) - Iterative (Using Stack)**
This approach uses a stack to simulate the recursive process iteratively.
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]  # Start with the root node

        while stack:
            node = stack.pop()  # Process the top node
            node.left, node.right = node.right, node.left  # Swap children

            if node.left:  # Add left child to the stack if it exists
                stack.append(node.left)
            if node.right:  # Add right child to the stack if it exists
                stack.append(node.right)

        return root  # Return the inverted tree
```

---

### **Summary**
- **BFS** is a level-by-level approach using a queue.
- **DFS (Recursive)** uses the natural call stack of the program.
- **DFS (Iterative)** uses an explicit stack to achieve the same behavior as recursion.

Each solution has the same time and space complexity. Choose based on your familiarity with recursion or iterative methods.
