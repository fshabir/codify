
from LinkedList import *
import unittest

def detect_loop(lst: LinkedList) -> bool:
    s = set()
    curr = lst.get_head()
    while curr:
        if curr.data in s:
            return True
        s.add(curr.data)
        curr = curr.next
    return False

class TestLoopDetection(unittest.TestCase):
    def test_detect_loop(self):
        lst = LinkedList()
        lst.insert(7)
        lst.insert(14)
        lst.insert(21)
        lst.insert(7)

        self.assertEqual(detect_loop(lst), True)


if __name__ == "__main__":
    unittest.main()