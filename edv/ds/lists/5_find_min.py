
class FindMinimum(object):
    def solution1(self, lst):
        if len(lst) == 0: return
        current_min = lst[0]
        for elm in lst:
            current_min = min(current_min, elm)
        return current_min

    def merge(self, lst1, lst2):
        res = []
        p1, p2 = 0, 0
        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] < lst2[p2]:
                res.append(lst1[p1])
                p1 += 1
            else:
                res.append(lst2[p2])
                p2 += 1

        while p1 < len(lst1):
            res.append(lst1[p1])
            p1 += 1

        while p2 < len(lst2):
            res.append(lst2[p2])
            p2 += 1
        return res

    def mergeSort(self, lst):
        if len(lst) == 1:
            return lst
        else:
            mid = len(lst) // 2
            left = self.mergeSort(lst[:mid])
            right = self.mergeSort(lst[mid:])
            return self.merge(left, right)

    def solution2(self, lst):
        lst = self.mergeSort(lst)
        return lst[0]

arr = [9,2,3,6]
print(f"Input => {arr}")
inst = FindMinimum()
print(f"Solution 1 => {inst.solution1(arr)}")
print(f"Solution 2 => {inst.solution2(arr)}")

inp = [2, 4, 10, 3, 5, 9, 0]
print(f"Merge sorting {inp} => {inst.mergeSort(inp)}")