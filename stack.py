class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Stack(object):
    def __init__(self, root=None):
        self.root = root

    def push(self, value):
        self.root = Node(value, self.root)

    def peek(self):
        if not self.is_empty():
            return self.root.value

    def pop(self):
        if not self.is_empty():
            value = self.root.value
            self.root = self.root.next
            return value
        else:
            return None

    def is_empty(self):
        return not self.root


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
for i in range(3):
    print(stack.peek())
    print(stack.pop())
