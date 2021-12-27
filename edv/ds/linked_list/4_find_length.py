
from LinkedList import *

def length(lst):
    len = 0
    curr = lst.get_head()
    while curr:
        len += 1
        curr = curr.next
    return len

lst = LinkedList()
lst.insert(0)
lst.insert(1)
lst.insert(2)
lst.insert(3)
lst.insert(4)
lst.print_list()

assert length(lst) == 5, "Should return 5"
