
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
    prev = None
    curr = lst.get_head()

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

        lst.head = prev
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