class Stack:

    def __init__(self):
        self.new_list = []

    def is_empty(self):
        if len(self.new_list) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.new_list.append(element)

    def pop(self):
        if self.is_empty() is True:
            return None
        else:
            return self.new_list.pop()


    def peek(self):
        if self.is_empty() is True:
            return None
        else:
            return self.new_list[-1]

    def size(self):
        return len(self.new_list)


