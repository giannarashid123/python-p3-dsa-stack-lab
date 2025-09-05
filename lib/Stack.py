class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        # Allow push regardless of full or not (overflow allowed)
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        # Returns distance from the top of the stack to the target element
        # Top element distance = 0
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                # distance from top = index difference
                return (len(self.items) - 1) - i
        return -1
