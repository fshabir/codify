
class RemoveEven(object):
    def solution1(self, lst):
        odds = []
        for elm in lst:
            if elm % 2 != 0:
                odds.append(elm)
        return odds

    def solution2(self, lst):
        return [elm for elm in lst if elm % 2 != 0]

my_list = [1,2,4,5,10,6,3]
print("Input => ", my_list)
inst = RemoveEven()
print("Solution 1 => ", inst.solution1(my_list))
print("Solution 2 => ", inst.solution2(my_list))