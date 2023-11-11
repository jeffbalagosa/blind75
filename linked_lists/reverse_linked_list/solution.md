# Solution

# Approach 1: Iterative

```python
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```

# Approach 2: Recursive

```python
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev
```
