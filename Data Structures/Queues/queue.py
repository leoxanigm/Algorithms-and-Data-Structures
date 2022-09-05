'''
    A basic implementation of a queue in python
'''


class Queue():
    def __init__(self):
        self.collection = list()

    @property
    def empty(self):
        return len(self.collection) == 0

    @property
    def head(self):
        if self.empty:
            return None
        else:
            return self.collection[0]

    @property
    def dequeue(self):
        if self.empty:
            raise Exception('Stack underflow')

        top = self.head
        self.collection = self.collection[1:]
        return top

    def enqueue(self, item):
        self.collection.append(item)

    def __repr__(self):
        return str(self.collection)


my_queue = Queue()
print(my_queue)
print(my_queue.empty)

my_queue.enqueue(1)
my_queue.enqueue(2)

print(my_queue.head)

my_queue.dequeue

print(my_queue.head)
print(my_queue.empty)
print(my_queue)