
from LinkedList import *

def delete(lst, val):
    curr = lst.get_head()
    if curr is None: return False
    if curr.data == val:
        lst.head = lst.head.next
        return True

    while curr.next and curr.next.data != val:
        curr = curr.next

    if curr.next is None:
        return False
    curr.next = curr.next.next
    return True


lst = LinkedList()
lst.insert(3)
lst.insert(2)
lst.insert(1)
lst.insert(0)

lst.print_list()

assert delete(lst, 3) == True, "Should return True"
lst.print_list()
assert delete(lst, 1) == True, "Should return True"
lst.print_list()
assert delete(lst, 5) == False, "Should return False"
lst.print_list()
assert delete(lst, 0) == True, "Should return True"
lst.print_list()
assert delete(lst, 2) == True, "Should return True"
lst.print_list()
