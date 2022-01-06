
from LinkedList import *
import unittest


def middle_node(lst: LinkedList) -> int:
    fast = lst.head
    if fast is None: return
    if fast.next is None:
        return fast.data

    slow = fast
    fast = fast.next.next

    while fast:
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

    return slow.data


class TestMiddleNode(unittest.TestCase):
    def setUp(self) -> None:
        self.lst = LinkedList()

    def test_middle_node_1(self):
        self.lst.head = None
        self.lst.insert(7)
        self.lst.insert(14)
        self.lst.insert(10)
        self.lst.insert(21)
        self.assertEqual(14, middle_node(self.lst))

    def test_middle_node_2(self):
        self.lst.head = None
        self.lst.insert(7)
        self.lst.insert(14)
        self.lst.insert(10)
        self.lst.insert(21)
        self.lst.insert(22)
        self.assertEqual(10, middle_node(self.lst))

    def test_middle_node_3(self):
        self.lst.head = None
        self.assertEqual(None, middle_node(self.lst))

    def test_middle_node_4(self):
        self.lst.head = None
        self.lst.insert(7)
        self.assertEqual(7, middle_node(self.lst))


if __name__ == "__main__":
    unittest.main()
