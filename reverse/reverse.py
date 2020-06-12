class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference  to the node we're currently at; update this as we traverse the list
        current = self.head


        # check to see if we are at a valid node
        while current:
            if current.get_value() == value:
                return True
        # update our current node to the current node next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        if node is not None:
            if node.get_next() == None:
                self.head = node
                self.head.next_node = prev
                return
            self.reverse_list(node.get_next(), node)
            node.next_node = prev

