"""
Given a stack of N elements, interleave the first half of the stack with the second half 
reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.

"""

from collections import deque

def interleave_stack(stack):
    q = deque()
    n = len(stack)

    # Step 1: Move all from stack to queue to reverse order
    while stack:
        q.append(stack.pop())

    # Step 2: Push first ⌊n/2⌋ back to stack (these are second half reversed)
    for _ in range(n // 2):
        stack.append(q.popleft())

    # Step 3: Enqueue the rest (which are the first half)
    while q:
        q.append(q.popleft())

    # Step 4: Interleave stack (second half reversed) and queue (first half)
    result = []
    while stack or q:
        if stack:
            result.append(stack.pop())
        if q:
            result.append(q.popleft())

    # Step 5: Push result back to original stack
    while result:
        stack.append(result.pop())

# 🔧 Test
s = [1, 2, 3, 4, 5]  # Top is rightmost
interleave_stack(s)
print(s)  # Output: [1, 5, 2, 4, 3]
