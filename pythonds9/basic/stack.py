"""Define a class object for Stacks and 
__len__
__bool__
__repr__ (“unambiguous representation of an object”)
__str__
__contains__  """

class Stack():
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def size(self):
    return len(self.items)

  def peek(self):
    if not self.items.is_empty():
      return self.items[-1]
    return 'Stack is empty'
  
  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def __str__(self):
    returnVal = "<Stack:"
    for item in self.items:
      returnVal += str(item)+ ";"
    returnVal += ">"
    return returnVal
  
  def __repr__(self):
    return "stack()"

  def __len__(self):
    return len(self.items)
    # return self.size()

  def __bool__(self):
    return self.items == []
    # return not self.is_empty()

def __contains__(self,item):
    return item in self.items
