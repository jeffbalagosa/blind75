# Solution

```Python
def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
    intervals = [Interval(start, end) for start, end in intervals]
    intervals.sort(key=lambda x: x.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False
    return True
```
