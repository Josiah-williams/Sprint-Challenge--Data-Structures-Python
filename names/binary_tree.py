class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if the value is less than the node's value
        if value < self.value:
            # if left is none
            if not self.left:
                # create new left node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:

            if not self.right:
                #insert the value on the right
             self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False

            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # check right side because it's at least equal to or greater than current root
        if self.right:
            # if there is a right node, repeat function
            return self.right.get_max()
        else:
            # if there isn't a right node, maximum value has been found
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if there is a left node
        if self.left:
            # call for each
            self.left.for_each(fn)
        # if there is a right node
        if self.right:
            # call for each
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # instantiate a queue
    #     queue = Queue()

    #     # enqueue our starting node (self)
    #     queue.enqueue(node)

    #     # while the queue has data
    #     while queue.size > 0:
    #         # dequeue the current node
    #         current = queue.dequeue()
    #         # print the nodes value
    #         if current is not None:
    #             print(current.value)
    #         # check if a left child exists
    #         if current.left:
    #             # enqueue left child
    #             queue.enqueue(current.left)
    #         if current.right:
    #             queue.enqueue(current.right)
            # check if right child exists
                # equeue right child

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # instantiate a stack
    #     stack = Stack()

    #     # push our starting node (self)
    #     stack.push(self)

    #     # while the stack has data
    #     while len(stack) > 0:
    #         # pop the current node
    #         current = stack.pop()
    #         # print the nodes 
    #         if current is not None:
    #             print(current.value)
    #         # check if a left child exists
    #         if current.left:
    #             # push left child
    #             stack.push(current.left)
    #         # check if right child exists
    #         if current.right:
    #             # push right child
    #             stack.push(current.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
