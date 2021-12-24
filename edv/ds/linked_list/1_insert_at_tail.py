import unittest
from LinkedList import LinkedList, Node

def insert_at_tail(lst: LinkedList, num: int):
    new_node = Node(num)
    curr = lst.get_head()

    while curr and curr.next is not None:
        curr = curr.next

    if curr is None:
        lst.head = new_node
    else:
        curr.next = new_node

lst = LinkedList()
lst.head = Node(4)
lst.head.next = Node(5)
insert_at_tail(lst, 6)

print(lst.print_list())