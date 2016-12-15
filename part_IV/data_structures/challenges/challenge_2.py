class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

list1 = [1, 2, 3, 4, 5]
list2 = []

stack = Stack()
for item in list1:
    stack.push(item)

for item in stack.items:
    list2.append(item)

print(list2)
