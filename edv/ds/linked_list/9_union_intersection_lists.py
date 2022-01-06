
from LinkedList import *
from collections import defaultdict

def union(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
    s = set()
    curr = lst1.head
    while curr:
        s.add(curr.data)
        curr = curr.next

    curr = lst2.head
    while curr:
        s.add(curr.data)
        curr = curr.next

    lst = LinkedList()
    for elm in s:
        lst.insert(elm)
    return lst


def intersection(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
    s = defaultdict(int)
    curr = lst1.head
    while curr:
        s[curr.data] += 1
        curr = curr.next

    curr = lst2.head
    while curr:
        s[curr.data] += 1
        curr = curr.next

    lst = LinkedList()
    for key, val in s.items():
        if val == 2:
            lst.insert(key)
    return lst

lst1 = LinkedList()
lst1.insert(10)
lst1.insert(20)
lst1.insert(80)
lst1.insert(60)

lst2 = LinkedList()
lst2.insert(15)
lst2.insert(20)
lst2.insert(30)
lst2.insert(60)
lst2.insert(45)

lst = union(lst1, lst2)
lst.print_list()

lst = intersection(lst1, lst2)
lst.print_list()