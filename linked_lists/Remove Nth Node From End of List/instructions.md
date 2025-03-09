# 19. Remove Nth Node From End of List

**Difficulty:** Medium

## Problem Statement

Given the `head` of a linked list, remove the `nᵗʰ` node from the end of the list and return its head.

---

## Example 1:

**Input:**
```plaintext
head = [1,2,3,4,5], n = 2
```
**Output:**
```plaintext
[1,2,3,5]
```
![Example 1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

---

## Example 2:

**Input:**
```plaintext
head = [1], n = 1
```
**Output:**
```plaintext
[]
```

---

## Example 3:

**Input:**
```plaintext
head = [1,2], n = 1
```
**Output:**
```plaintext
[1]
```

---

## Constraints:

- The number of nodes in the list is `sz`.
- `1 ≤ sz ≤ 30`
- `0 ≤ Node.val ≤ 100`
- `1 ≤ n ≤ sz`

---

## Follow-up:

Can you solve this problem in one pass?

---

## Related Topics

- [Linked List](https://leetcode.com/tag/linked-list/)
- [Two Pointers](https://leetcode.com/tag/two-pointers/)

---

## Hint

Maintain two pointers and update one with a delay of `n` steps.
