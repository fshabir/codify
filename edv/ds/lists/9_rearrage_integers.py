
class ReArranger(object):
    def solution1(self, lst):
        return sorted(lst)

    def solution2(self, lst):
        neg = []
        pos = []
        for elm in lst:
            if elm < 0:
                neg.append(elm)
            else:
                pos.append(elm)
        return neg + pos

    def solution3(self, lst):
        return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

    def solution4(self, lst):
        leftMostPos = 0
        for i, elm in enumerate(lst):
            if elm < 0:
                lst[i], lst[leftMostPos] = lst[leftMostPos], lst[i]
                leftMostPos += 1
        return lst


def test_solution1(inst):
    assert inst.solution1([10,-1,20,4,5,-9,-6]) in ([-1, -9, -6, 10, 20, 4, 5], [-9, -6, -1, 4, 5, 10, 20])

def test_solution2(inst):
    assert inst.solution2([10,-1,20,4,5,-9,-6]) in (
        [-1, -9, -6, 10, 20, 4, 5],
        [-9, -6, -1, 4, 5, 10, 20],
        [-1, -9, -6, 4, 5, 10, 20]
    )

def test_solution3(inst):
    assert inst.solution3([10,-1,20,4,5,-9,-6]) in (
        [-1, -9, -6, 10, 20, 4, 5],
        [-9, -6, -1, 4, 5, 10, 20],
        [-1, -9, -6, 4, 5, 10, 20]
    )

def test_solution4(inst):
    assert inst.solution4([10,-1,20,4,5,-9,-6]) in (
        [-1, -9, -6, 10, 20, 4, 5],
        [-9, -6, -1, 4, 5, 10, 20],
        [-1, -9, -6, 4, 5, 10, 20]
    )


if __name__ == "__main__":
    inst = ReArranger()
    test_solution1(inst)
    test_solution2(inst)
    test_solution3(inst)
    test_solution4(inst)