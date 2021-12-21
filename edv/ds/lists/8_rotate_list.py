
class ListRotator(object):
    def solution1(self, lst, k):
        if len(lst) < k:
            k %= k % len(lst)
        return lst[-k:] + lst[:-k]

    def solution2(self, lst, k):
        if len(lst) < k:
            k %= len(lst)
        res = []
        idx = len(lst) - k
        while len(res) != len(lst):
            res.append(lst[idx])
            idx += 1
            if idx > len(lst):
                idx = 0
        return res

lst = [10,20,30,40,50]
# lst = ['right', 'rotate', 'python']
print(f"Input => {lst}")

inst = ListRotator()
print(f"Solution 1 => {inst.solution1(lst, 1)}")
print(f"Solution 2 => {inst.solution1(lst, 1)}")