
class TwoSum(object):
    def solution1(self, lst, k):
        p1 = 0
        while p1 < len(lst):
            p2 = 0
            while p2 < len(lst):
                if p1 != p2 and lst[p1] + lst[p2] == k:
                    return [lst[p1], lst[p2]]
                p2 += 1
            p1 += 1

    def solution2(self, lst, k):
        lst.sort()
        p1, p2 = 0, len(lst) - 1
        while p1 < p2:
            if lst[p1] + lst[p2] > k:
                p2 -= 1
            elif lst[p1] + lst[p2] < k:
                p1 += 1
            else:
                return [lst[p1], lst[p2]]

    def binary_search(self, lst, num):
        start = 0
        end = len(lst) - 1
        while start <= end:
            mid = (start + end) // 2
            if lst[mid] == num:
                return mid
            elif lst[mid] < num:
                start = mid + 1
            else:
                end = mid - 1

    def solution3(self, lst, k):
        """
        Sort the list and then use binary search to find the k - a[i] element
        :param lst: List of integers
        :param k: Desired sum
        :return: list of 2 elements that equal k from provided lst
        """
        lst.sort()
        for idx, elm in enumerate(lst):
            idx_remainder = self.binary_search(lst, k - elm)
            if idx_remainder and idx_remainder != idx:
                return [lst[idx], lst[idx_remainder]]


lst = [1,21,3,14,5,60,7,6]
k = 81

print(f"List => {lst}, k => {k}")
inst = TwoSum()

print(f"Solution 1 => {inst.solution1(lst, k)}")
print(f"Solution 2 => {inst.solution2(lst, k)}")
print(f"Solution 3 => {inst.solution3(lst, k)}")

print(f"Binary search 3 in [1, 2, 3, 4, 5] => {inst.binary_search([1, 2, 3, 4, 5], 4)}")
print(f"Binary search 5 in [1, 3, 5, 6, 7, 14, 21, 60] => {inst.binary_search([1, 3, 5, 6, 7, 14, 21, 60], 5)}")