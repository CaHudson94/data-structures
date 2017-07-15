"""Python implementation of Binary Search Tree."""
from timeit import timeit


class BST(object):
    """Binary Search Tree."""

    def __init__(self, iterable=None):
        """Initialize Binary Search tree."""
        self._root = None
        self._length = 0
        self._rdepth = 0
        self._ldepth = 0
        self._depth = 0
        self._balance = 0
        if type(iterable) in [tuple, list]:
            for i in iterable:
                if type(i) in [int, float]:
                    self.insert(i)
                else:
                    raise TypeError('''
Try again with only numbers in your list or tuple.''')
        elif type(iterable) == int:
            self.insert(iterable)
        elif iterable is not None:
            raise TypeError('Try again with a list, tuple, int, or float.')

    def insert(self, val):
        """Insert new node into Binary Search Tree."""
        if type(val) not in [int, float]:
            raise TypeError('You can only add numbers to this tree.')
        curr = self._root
        if curr is None:
            curr = Node(val)
            self._root = curr
            self._length = 1
            self._depth = 1
            return
        while True:
            if val < curr.val:
                if iteration == 0:
                        iteration += 1
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    curr.left.parent = curr
                    self._length += 1
                    self._depth_and_bal(self._root)
                    return
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    curr.right.parent = curr
                    self._length += 1
                    self._depth_and_bal(self._root)
                    return

    def _tree_depth(self, node):
        """Get the depth of the tree or sub tree."""
        lside = {}
        rside = {}
        on_right = False
        curr = None
        if node.left:
            curr = node.left
        elif node.right:
            curr = node.right
        while True:
            if curr == node.right:
                on_right = True
            elif not node.left:
                on_right = True
            if curr == node and curr.left and curr.left in lside.keys():
                    curr = curr.right
                    on_right = True
            elif on_right:
                if curr not in rside.keys() and curr.parent in rside.keys():
                    rside[curr] = rside[curr.parent] + 1
                elif curr == node.right:
                    rside[curr] = 1
                if curr.left and curr.left not in rside.keys():
                    curr = curr.left
                elif curr.right and curr.right not in rside.keys():
                    curr = curr.right
                else:
                    curr = curr.parent
            else:
                if curr not in lside.keys() and curr.parent in lside.keys():
                    lside[curr] = lside[curr.parent] + 1
                elif curr == node.left:
                    lside[curr] = 1
                if curr.left and curr.left not in lside.keys():
                    curr = curr.left
                elif curr.right and curr.right not in lside.keys():
                    curr = curr.right
                else:
                    curr = curr.parent
            if on_right or not node.right:
                if curr == node:
                    if rside and lside:
                        return (max(rside.values()),
                                max(lside.values()))
                    elif rside:
                        return (max(rside.values()), 0)
                    else:
                        return (0, max(lside.values()))

    def _depth_and_bal(self, node):
        """Get the new depth and balance of the tree."""
        depth = self._tree_depth(node)
        self._rdepth = depth[0]
        self._ldepth = depth[1]
        self._balance = self._rdepth - self._ldepth
        self._depth = max([self._rdepth, self._ldepth]) + 1

    def search(self, val):
        """Find the node at val in Binary Search Tree."""
        curr = self._root
        if type(val) not in [int, float]:
            raise TypeError('This tree only contains numbers.')
        while True:
            if curr is None:
                return None
            elif val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right

    def size(self):
        """Return the amount of nodes in Binary Search Tree."""
        return self._length

    def depth(self):
        """Return the levels of the Binary Search Tree."""
        return self._depth

    def contains(self, val):
        """Return true if specified val is in tree, false if it is not."""
        if type(val) not in [int, float]:
            raise TypeError('This tree only contains numbers.')
        if self.search(val):
            return True
        return False

    def balance(self):
        """Return the difference of left and right depth from root."""
        return self._balance

    def in_order(self):
        """Return generator that returns values from BST 'in order'."""
        nodes = []
        curr = self._root
        while len(nodes) != self._length:
            if not curr.right and not curr.left and not curr.parent:
                nodes.append(curr)
            elif curr.left and curr.left not in nodes:
                curr = curr.left
            elif curr not in nodes:
                nodes.append(curr)
                if curr.right and curr.right not in nodes:
                    curr = curr.right
                else:
                    curr = curr.parent
            else:
                curr = curr.parent
        for node in nodes:
            yield node.val

    def pre_order(self):
        """Return generator that returns values from BST 'pre ordered'."""
        nodes = []
        curr = self._root
        while len(nodes) != self._length:
            if curr not in nodes:
                nodes.append(curr)
            if curr.left and curr.left not in nodes:
                curr = curr.left
            elif curr.right and curr.right not in nodes:
                curr = curr.right
            else:
                curr = curr.parent
        for node in nodes:
            yield node.val

    def post_order(self):
        """Return generator that returns values from BST 'post ordered'."""
        nodes = []
        curr = self._root
        while len(nodes) != self._length:
            if not curr.right and not curr.left and not curr.parent:
                nodes.append(curr)
            elif curr.left and curr.left not in nodes:
                curr = curr.left
            elif curr.right and curr.right not in nodes:
                curr = curr.right
            else:
                nodes.append(curr)
                curr = curr.parent
        for node in nodes:
            yield node.val

    def breadth_first(self):
        """Return generator that returns values from BST 'breadth first'."""
        nodes = []
        curr_index = 0
        nodes.append(self._root)
        while len(nodes) != self._length:
            if nodes[curr_index].left:
                nodes.append(nodes[curr_index].left)
            if nodes[curr_index].right:
                nodes.append(nodes[curr_index].right)
            curr_index += 1
        for node in nodes:
            yield node.val


class Node(object):
    """Create a node to add to the Binary Search Tree."""

    def __init__(self, val, left=None, right=None):
        """Initialize a new node."""
        self.val = val
        self.left = left
        self.right = right


def wrapper(func, *args, **kwargs):  # pragma: no cover
    """Create a value for a function with a specific arguement called to it."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped
    #  code found through Erik Enderlein
    #  he found it at http://pythoncentral.io/time-a-python-function/


if __name__ == '__main__':  # pragma: no cover
    best_stuff_tree = BST()
    find5 = wrapper(best_stuff_tree.search, 5)
    find24 = wrapper(best_stuff_tree.search, 24)
    nodes = [5, 3, 8, 2.2, 4, 9.5, 1, 2.6,
             3.3, 4.5, 9, 11, 8.5, 10, 14,
             16, 15, 21, 23, 24]
    for node in nodes:
        best_stuff_tree.insert(node)
    print(timeit(find5))
    print(timeit(find24))
