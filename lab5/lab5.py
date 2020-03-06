import time


class Node:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insert(self, node, curr_node=None):
        if curr_node is None:
            curr_node = self.root
        if node.data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = node
            else:
                return self.insert(node, curr_node.left)
        elif node.data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = node
            else:
                return self.insert(node, curr_node.right)

    def search(self, val, curr_node=None):
        if curr_node is None:
            curr_node = self.root
            global start
            start = time.perf_counter()
        if curr_node.data == val:
            end = time.perf_counter()
            print(end - start)
            return True
        elif curr_node.data > val:
            if curr_node.left:
                return self.search(val, curr_node.left)
            else:
                end = time.perf_counter()
                print(end - start)
                return False
        else:
            if curr_node.right:
                return self.search(val, curr_node.right)
            else:
                end = time.time()
                print(end - start)
                return False

def constructBST(filename):
    f = open(filename, 'r')
    foo = f.read().split()
    #print(foo)
    root = Node(foo[0])
    bst = BinarySearchTree(root)
    for i in range(1, len(foo)):
        #print(foo[i])
        curr_node = Node(foo[i])
        bst.insert(curr_node)
    return bst
