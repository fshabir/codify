
class MaxMin(object):
    def solution1(self, lst):
        if len(lst) <= 1: return lst
        res = []
        start, end = 0, len(lst) - 1
        while start < end:
            res.append(lst[end])
            end -= 1
            res.append(lst[start])
            start += 1

        if start == end:
            res.append(lst[start])
        return res

def test_solution1(inst):
    assert inst.solution1([1,2,3,4,5]) == [5,1,4,2,3], "Should be [5,1,4,2,3]"

if __name__ == "__main__":
    inst = MaxMin()
    test_solution1(inst)