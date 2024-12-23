### Extracted Content:

# 121. Best Time to Buy and Sell Stock - Explanation

## Description
You are given an integer array `prices`, where `prices[i]` represents the price of NeetCoin on the `i`th day.

You may:
- Choose a **single day** to buy one NeetCoin.
- Choose a **different day in the future** to sell it.

Return the **maximum profit** you can achieve. If no transactions are profitable, return `0`.

---

### Example 1:
**Input**:
`prices = [10, 1, 5, 6, 7, 1]`

**Output**:
`6`

**Explanation**:
- Buy on day 2 (price = 1).
- Sell on day 5 (price = 7).
Profit = `7 - 1 = 6`.

---

### Example 2:
**Input**:
`prices = [10, 8, 7, 5, 2]`

**Output**:
`0`

**Explanation**:
- No profitable transactions can be made.
Maximum profit = `0`.

---

### Constraints:
- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`

---

### Recommended Time & Space Complexity:
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

---

### Hints:
1. **Brute Force**:
   A naive solution is to iterate through all possible combinations of buying and selling days, which results in a time complexity of `O(n^2)`.

2. **Optimized Solution**:
   To optimize, consider iterating through the array once while keeping track of:
   - The **minimum price** seen so far (to buy).
   - The **maximum profit** based on the difference between the current price and the minimum price.

---

### Solution Approaches:

#### 1. Brute Force
**Code (Python):**
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                res = max(res, sell - buy)
        return res
```
**Time Complexity**: `O(n^2)`
**Space Complexity**: `O(1)`

---

#### 2. Two Pointers
**Code (Python):**
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l = buy, r = sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
```
**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

---

#### 3. Dynamic Programming
**Code (Python):**
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
```
**Time Complexity**: `O(n)`
**Space Complexity**: `O(1)`

---

### Video Explanation
For an in-depth explanation, check out the [video tutorial](https://www.youtube.com/embed/1pkOgXD63yU).
