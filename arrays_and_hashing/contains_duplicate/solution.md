# Solution

```Python
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

Time complexity: O(n) where n is the length of nums.
