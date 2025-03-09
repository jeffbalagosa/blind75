# 143. Reorder List

**Difficulty:** Medium

## Problem Statement

You are given the head of a singly linked list. The list can be represented as:

```
L₀ → L₁ → … → Lₙ₋₁ → Lₙ
```

Reorder the list to be in the following form:

```
L₀ → Lₙ → L₁ → Lₙ₋₁ → L₂ → Lₙ₋₂ → …
```

You may not modify the values in the list’s nodes. Only nodes themselves may be changed.

---

## Example 1:

**Input:**
```plaintext
head = [1,2,3,4]
```
**Output:**
```plaintext
[1,4,2,3]
```
![Example 1](https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg)

---

## Example 2:

**Input:**
```plaintext
head = [1,2,3,4,5]
```
**Output:**
```plaintext
[1,5,2,4,3]
```
![Example 2](https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg)

---

## Constraints:

- The number of nodes in the list is in the range **[1, 5 × 10⁴]**.
- `1 ≤ Node.val ≤ 1000`

---

## Related Topics

- [Linked List](https://leetcode.com/tag/linked-list/)
- [Two Pointers](https://leetcode.com/tag/two-pointers/)
- [Stack](https://leetcode.com/tag/stack/)
- [Recursion](https://leetcode.com/tag/recursion/)
