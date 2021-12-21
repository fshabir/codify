
class SecondLargest(object):
    def solution1(self, lst):
        if len(lst) <= 2: return
        lst.sort()
        return lst[-2]

    def solution2(self, lst):
        if len(lst) < 2: return
        idx = 0
        firstLargest = lst[idx]
        secondLargest = None
        idx += 1
        while idx < len(lst):
            curr = lst[idx]
            if secondLargest is None and curr != firstLargest:
                secondLargest = curr
            elif curr > firstLargest:
                secondLargest = firstLargest
                firstLargest = curr
            idx += 1
        return secondLargest

    def solution3(self, lst):
        if len(lst) < 2: return
        first_max, second_max = float('-inf'), float('-inf')
        for elm in lst:
            if elm > first_max:
                second_max = first_max
                first_max = elm
            elif elm > second_max and elm != first_max:
                second_max = elm
        return second_max if second_max != float('-inf') else None


arr = [9,2,3,6]
arr = [4, 4, 4, 4]
print(f"Input => {arr}")

inst = SecondLargest()
print(f"Solution 1 => {inst.solution1(arr)}")
print(f"Solution 2 => {inst.solution2(arr)}")
print(f"Solution 3 => {inst.solution3(arr)}")