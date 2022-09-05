'''
    A basic implementation of a stack in python
'''


class Stack():
    def __init__(self):
        self.container = list()

    @property
    def empty(self):
        return len(self.container) == 0

    @property
    def top(self):
        if self.empty:
            return None
        else:
            return self.container[-1]

    @property
    def pop(self):
        if self.empty:
            raise Exception('Stack empty')

        last = self.top
        self.container = self.container[:-1]
        return last

    def push(self, item):
        self.container.append(item)

    def __repr__(self):
        return str(self.container)


my_stack = Stack()
print(my_stack)
print(my_stack.empty)

my_stack.push(1)
my_stack.push(2)

print(my_stack.top)

my_stack.pop

print(my_stack.top)
print(my_stack.empty)
print(my_stack)
