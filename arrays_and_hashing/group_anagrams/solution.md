# Solution

```Python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = collections.defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(string)
        return result.values()
```

Time complexity: O(nk) where n is the length of strs and k is the maximum length of a string in strs.
