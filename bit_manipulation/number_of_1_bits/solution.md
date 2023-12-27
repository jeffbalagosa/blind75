# Solution

```Python
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n > 0:
            result += n % 2
            n = n >> 1
        return result
```

Time complexity: O(1) since n is a 32-bit integer.
