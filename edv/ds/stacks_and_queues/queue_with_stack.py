

class Queue(object):
    def __init__(self):
        self.size = 0
        self.stack = []

    def enqueue(self, value):
        self.stack.append(value)

    def dequeue(self):
        temp_stack = self.stack[::-1]
        returnValue = temp_stack.pop()
        self.stack = temp_stack[::-1]
        return returnValue

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

