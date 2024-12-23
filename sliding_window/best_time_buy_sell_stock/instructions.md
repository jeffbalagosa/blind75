# 121. Best Time to Buy and Sell Stock

## Level: Easy

## Description

You are given an array `prices`, where `prices[i]` represents the price of a stock on the `i`th day.

Your objective is to maximize your profit by:
- Choosing a **single day** to buy one stock.
- Choosing a **later day** in the future to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If no profit can be made, return `0`.

### Example 1:

**Input**:
`prices = [7,1,5,3,6,4]`

**Output**:
`5`

**Explanation**:
- Buy on day 2 (price = 1).
- Sell on day 5 (price = 6).
Profit = `6 - 1 = 5`.
**Note**: You cannot sell a stock before you buy it.

---

### Example 2:

**Input**:
`prices = [7,6,4,3,1]`

**Output**:
`0`

**Explanation**:
- No profitable transactions can be made in this case.
- Maximum profit = `0`.

---

### Constraints:

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
