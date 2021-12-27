
from LinkedList import *

def reverse(lst: LinkedList) -> LinkedList:
    stack = list()
    curr = lst.get_head()
    while curr:
        stack.append(curr.data)
        curr = curr.next

    new_list = LinkedList()
    while len(stack):
        new_list.insert(stack.pop())

    return new_list

def reverse_in_place(lst: LinkedList) -> LinkedList:
    p1, p2, p3 = (None, None, None)
    p2 = lst.get_head()
    if p2 is None: return None
    p3 = p2.next

    while p3:
        p2.next = p1
        p1 = p2
        p2 = p3
        p3 = p3.next

    p2.next = p1
    lst.head = p2
    return lst


lst = LinkedList()
lst.insert(0)
lst.insert(1)
lst.insert(2)
lst.insert(3)
lst.insert(4)

lst.print_list()

new_list = reverse_in_place(lst)
new_list.print_list()