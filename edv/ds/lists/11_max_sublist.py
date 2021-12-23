
import unittest

class MaxSubList(object):
    def solution1(self, lst):
        if len(lst) == 0: return
        if len(lst) == 1: return lst[0]

        current_max = lst[0]
        global_max = lst[0]

        for i in range(1, len(lst)):
            if current_max < 0:
                current_max = lst[i]
            else:
                current_max += lst[i]
            global_max = max(current_max, global_max)

        return global_max


class TestMaxSubList(unittest.TestCase):
    def test_solution1(self):
        inst = MaxSubList()
        self.assertEqual(inst.solution1([-4, 2, -5, 1, 2, 3, 6, -5, 1]), 12)


if __name__ == "__main__":
    unittest.main()