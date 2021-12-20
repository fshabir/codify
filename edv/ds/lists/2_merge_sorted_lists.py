
class MergeSortedLists(object):
    def solution1(self, lst1, lst2):
        final_lst = []
        p1 = p2 = 0
        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] < lst2[p2]:
                final_lst.append(lst1[p1])
                p1 += 1
            else:
                final_lst.append(lst2[p2])
                p2 += 1

        while p1 < len(lst1):
            final_lst.append(lst1[p1])
            p1 += 1

        while p2 < len(lst2):
            final_lst.append(lst2[p2])
            p2 += 1

        return final_lst

    def solution2(self, lst1, lst2):
        final_lst = lst1 + lst2
        final_lst.sort()
        return final_lst

    def solution3(self, lst1, lst2):
        """
        Merges both lists in-place
        :param lst1: first list of integers
        :param lst2: second list of integers
        :return: merged and sorted list of integers
        """
        p1 = p2 = 0
        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] > lst2[p2]:
                lst1.insert(p1, lst2[p2])
                p2 += 1
                # p1 needs to be incremented because list1 gets extended
                # and after adding 1 element, pointer should be incremented
                # to point to the element before the insertion
                p1 += 1
            else:
                p1 += 1

        if p2 < len(lst2):
            lst1.extend(lst2[p2:])

        return lst1

# list1 = [1,3,4,5]
# list2 = [2,6,7,8]

list1, list2 = [4, 5, 6], [-2, -1, 0, 7]

print(f"List 1 => {list1}")
print(f"List 2 => {list2}")

inst = MergeSortedLists()
print(f"Solution 1 => {inst.solution1(list1, list2)}")
print(f"Solution 2 => {inst.solution2(list1, list2)}")
print(f"Solution 3 => {inst.solution3(list1, list2)}")