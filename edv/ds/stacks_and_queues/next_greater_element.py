
from typing import List


def next_greater_element(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        changed = False
        for j in range(i+1, len(lst)):
            if lst[i] < lst[j]:
                lst[i] = lst[j]
                changed = True
                break
        if changed is False:
            lst[i] = -1
    return lst


def next_greater_element_2(lst: List[int]) -> List[int]:
    stack = []
    for i in range(len(lst)-1, -1, -1):
        while len(stack) > 0 and stack[-1] <= lst[i]:
            stack.pop()

        curr = lst[i]
        if len(stack) == 0:
            lst[i] = -1
        else:
            lst[i] = stack[-1]
        stack.append(curr)
    return lst


print(f"next_greater_element([4, 6, 3, 2, 8, 1]) => {next_greater_element([4, 6, 3, 2, 8, 1])}")
print(f"next_greater_element_2([4, 6, 3, 2, 8, 1]) => {next_greater_element_2([4, 6, 3, 2, 8, 1])}")