
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value)

    def is_empty(self):
        return self.head is None

    def print_list(self):
        curr = self.head
        print("List: ", end="")
        while curr is not None:
            print(curr.data, end = " => ")
            curr = curr.next
        print("None")


