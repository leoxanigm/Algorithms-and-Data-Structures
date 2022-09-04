'''
    A basic implementation of a vector in python
'''


class Vector():
    def __init__(self, len):
        self.container = [None] * len

    @property
    def length(self):
        return len(self.container)

    def select(self, index):
        return self.container[index]

    def store(self, item, index):
        self.container[index] = item

    def __repr__(self):
        return str(self.container)


myVec = Vector(5)
myVec.store(3, 2)
print(myVec)
print(myVec.length)
print(myVec.select(2))
