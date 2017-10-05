class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

    def getItem(self):
        return self.item

    def __str__(self):
        try:
            return str(self.item)
        except TypeError:
            print "item is not an type that can be changed to str"
        else:
            print Exception
            return

node1 = Node(2.3)
node2 = Node(2)
node1.next = node2
print (node1.getItem)
print (node2.getItem)
        