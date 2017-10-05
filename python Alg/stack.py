class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(itme)

    def isEmpty(self):
        if self.items == []:
            return True
        return False

    def pop(self):
        if not self.items == []:
            return self.items.pop()
        else:
            return None