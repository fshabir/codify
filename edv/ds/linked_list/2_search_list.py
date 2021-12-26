
from LinkedList import LinkedList, Node

def search(lst, value):
    curr = lst.get_head()
    while curr:
        if curr.data == value:
            return True
        curr = curr.next
    return False

lst = LinkedList()
lst.insert(5)
lst.insert(90)
lst.insert(10)
lst.insert(4)

lst.print_list()

assert search(lst, 4) == True, "List search should return true"
assert search(lst, 5) == True, "List search should return true"
assert search(lst, 50) == False, "List search should return false"
