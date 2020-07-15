class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return "deque()"

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return self.items == []
        # return not self.is_empty()

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        returnVal = "<Deque:"
        for item in self.items:
            returnVal += str(item) + ";"
        returnVal += ">"
        return returnVal
