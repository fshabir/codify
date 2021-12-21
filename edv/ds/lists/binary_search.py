
class BinarySearch(object):
    def method1(self, lst, num):
        start, end = 0, len(lst) - 1
        while start <= end:
            mid = (start + end) // 2
            if lst[mid] == num:
                return mid
            elif lst[mid] < num:
                start = mid + 1
            else:
                end = mid - 1

    def __recurse(self, lst, start, end, num):
        mid = (start + end) // 2
        if start > end:
            return
        elif lst[mid] == num:
            return mid
        elif lst[mid] < num:
            return self.__recurse(lst, mid + 1, end, num)
        else:
            return self.__recurse(lst, start, mid - 1, num)

    def method2(self, lst, num):
        return self.__recurse(lst, 0, len(lst) - 1, num)


inp = [1, 2, 3, 4, 5]
num = 3
print(f"Input => List: {inp}, Num: {num}")
inst = BinarySearch()
print(f"Solution 1 with Num {num} => {inst.method1(inp, num)}")
print(f"Solution 2 with Num {num} => {inst.method2(inp, num)}")
num = 2
print(f"Solution 1 with Num {num} => {inst.method1(inp, num)}")
print(f"Solution 2 with Num {num} => {inst.method2(inp, num)}")
num = 0
print(f"Solution 1 with Num {num} => {inst.method1(inp, num)}")
print(f"Solution 2 with Num {num} => {inst.method2(inp, num)}")
num = 7
print(f"Solution 1 with Num {num} => {inst.method1(inp, num)}")
print(f"Solution 2 with Num {num} => {inst.method2(inp, num)}")
num = 1
print(f"Solution 1 with Num {num} => {inst.method1(inp, num)}")
print(f"Solution 2 with Num {num} => {inst.method2(inp, num)}")
num = 5
print(f"Solution 1 with Num {num} => {inst.method1(inp, num)}")
print(f"Solution 2 with Num {num} => {inst.method2(inp, num)}")