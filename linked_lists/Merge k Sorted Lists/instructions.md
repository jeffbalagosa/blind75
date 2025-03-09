# 23. Merge k Sorted Lists

**Difficulty:** Hard

## Problem Statement

You are given an array of `k` linked lists, each sorted in ascending order.

Merge all the linked lists into one sorted linked list and return it.

---

## Example 1:

**Input:**
```plaintext
lists = [[1,4,5],[1,3,4],[2,6]]
```
**Output:**
```plaintext
[1,1,2,3,4,4,5,6]
```
**Explanation:**
The linked lists are:
```
[
  1->4->5,
  1->3->4,
  2->6
]
```
Merging them into one sorted list:
```
1->1->2->3->4->4->5->6
```

---

## Example 2:

**Input:**
```plaintext
lists = []
```
**Output:**
```plaintext
[]
```

---

## Example 3:

**Input:**
```plaintext
lists = [[]]
```
**Output:**
```plaintext
[]
```

---

## Constraints:

- `k == lists.length`
- `0 ≤ k ≤ 10⁴`
- `0 ≤ lists[i].length ≤ 500`
- `-10⁴ ≤ lists[i][j] ≤ 10⁴`
- Each `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10⁴`.

---

## Related Topics

- [Linked List](https://leetcode.com/tag/linked-list/)
- [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/)
- [Heap (Priority Queue)](https://leetcode.com/tag/heap-priority-queue/)
- [Merge Sort](https://leetcode.com/tag/merge-sort/)
