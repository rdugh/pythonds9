"""Define a class object for Queues and
__len__
__bool__
__repr__ (“unambiguous representation of an object”)
__str__
__contains__  
by Ravi Dugh"""


class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return 'Queue is empty'        
           
    def __str__(self):
        returnVal = "<Queue:"
        for item in self.items:
            returnVal += str(item) + ";"
        returnVal += ">"
        return returnVal

    def __repr__(self):
        return "queue()"

    def __len__(self):
        return len(self.items)
        # return self.size()

    def __bool__(self):
        return self.items == []
        # return not self.is_empty()

    def __contains__(self, item):
        return item in self.items
