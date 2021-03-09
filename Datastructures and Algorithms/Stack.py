"""
This program implements the basic stack data structure using python lists
"""


class Stack:

    def __init__(self, n=-1):
        self.size = n
        self.stack = []
        self.pointer = -1

    def push(self, element):
        if self.isfull():
            print("Stack is Full")
        else:
            self.pointer = self.pointer + 1
            self.stack.append(element)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            try:
                item = self.stack.pop(self.pointer)
                self.pointer = self.pointer - 1
                return item
            except IndexError:
                print("Exception: Stack is empty")


    def isempty(self):
        if self.pointer == -1:
            return True
        else:
            return False

    def isfull(self):
        if self.size == -1:
            return False
        elif self.pointer == self.size - 1:
            return True
        else:
            return False

    def print_stack(self):
        print(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.print_stack()
    s.push(5)
    s.push("car")
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()
