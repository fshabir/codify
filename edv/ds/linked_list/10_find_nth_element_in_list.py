
from LinkedList import *

def find_nth_element_from_end(lst: LinkedList, n: int) -> int:
    target_element = lst.get_length() - n
    counter = 0
    curr = lst.head
    while curr:
        if counter == target_element:
            return curr.data
        curr = curr.next
        counter += 1
    return -1

lst = LinkedList()
lst.insert(15)
lst.insert(22)
lst.insert(8)
lst.insert(7)
lst.insert(14)
lst.insert(21)
print(find_nth_element_from_end(lst, 4))