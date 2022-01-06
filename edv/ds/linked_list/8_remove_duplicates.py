
from LinkedList import *

def remove_duplicates(lst: LinkedList) -> LinkedList:
    s = set()
    curr = lst.head
    while curr:
        s.add(curr.data)
        next = curr.next
        while next and next.data in s:
            next = next.next
        curr.next = next
        curr = next
    return lst

def remove_duplicates_2(lst: LinkedList) -> LinkedList:
    curr = lst.head
    while curr:
        next = curr.next
        while next and next.data == curr.data:
            next = next.next
        curr.next = next
        curr = curr.next
    return lst


lst = LinkedList()
lst.insert(1)
lst.insert(2)
lst.insert(2)
lst.insert(2)
lst.insert(3)
lst.insert(4)
lst.insert(4)
lst.insert(5)
lst.insert(6)

lst.print_list()
lst = remove_duplicates(lst)
lst.print_list()

lst2 = LinkedList()
lst2.insert()