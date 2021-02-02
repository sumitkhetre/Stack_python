class Stack:

    def __init__(self):
        self.stack = []

    def printStack(self):
        for n in self.stack:
            print(n)

    def add(self, dataval):
        # Use list append method to add element

        if len(self.stack) == 0:
            self.stack.append(dataval)
        else:
           self.stack.append(dataval)

        # if dataval not in self.stack:
        #     self.stack.append(dataval)
        #     return True
        # else:
        #     return False

    # Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()


AStack = Stack()
AStack.add("Mon")

AStack.add("Mon")

AStack.add("Mon")

AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.printStack())
print(AStack.remove())
print(AStack.remove())