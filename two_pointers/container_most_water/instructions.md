# Leetcode Problem: 11. Container With Most Water

## Difficulty: Medium

## Description
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i<sup>th</sup>` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

---

## Example 1:
![Example 1 Image](./assets/question_11.jpg)

**Input**:
```
height = [1,8,6,2,5,4,8,3,7]
```
**Output**:
```
49
```
**Explanation**:
The vertical lines are represented by the array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is 49.


---

## Example 2:
**Input**:
```
height = [1,1]
```
**Output**:
```
1
```

---

## Constraints:
1. `n == height.length`
2. `2 <= n <= 10^5`
3. `0 <= height[i] <= 10^4`

---

## Hint
- Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
