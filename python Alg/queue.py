class queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def delete(self):
        itemToDelete = self.items[0]
        del self.items[0]
        return itemToDelete

    def size(self):
        return len(self.items)

    def report (self):
        return self.items
