class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self._data = data
        self._parent = parent
        self._left = left
        self._right = right

    @property
    def data(self):
        return self._data

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def set_data(self, value):
        self._data = value

    def set_parent(self, value):
        self._parent = value

    def set_left(self, value):
        self._left = value

    def set_right(self, value):
        self._right = value


class BinaryTree:
    def __init__(self, data=None):
        self.root = Node(data)
        self.tree_list = []

    def insert(self, elem, root=None):
        if not root:
            root = self.root

        if not root.data:
            root._data = elem
        else:
            if elem <= root.data:
                if root.left:
                    self.insert(elem, root.left)
                else:
                    root.set_left(Node(elem, root))
            else:
                if root.right:
                    self.insert(elem, root.right)
                else:
                    root.set_right(Node(elem, root))

    def in_order(self, root=None):
        list_tree = []
        if not root:
            root = self.root

        if root.left:
            list_tree.extend(self.in_order(root.left))

        list_tree.append(root.data)

        if root.right:
            list_tree.extend(self.in_order(root.right))

        return list_tree

    def pre_order(self, root=None):
        list_tree = []
        if not root:
            root = self.root

        list_tree.append(root.data)

        if root.left:
            list_tree.extend(self.pre_order(root.left))

        if root.right:
            list_tree.extend(self.pre_order(root.right))

        return list_tree

    def post_order(self, root=None):
        list_tree = []
        if not root:
            root = self.root

        if root.left:
            list_tree.extend(self.post_order(root.left))

        if root.right:
            list_tree.extend(self.post_order(root.right))

        list_tree.append(root.data)

        return list_tree


if __name__ == '__main__':
    bt = BinaryTree()

    bt.insert(11)
    bt.insert(9)
    bt.insert(15)
    bt.insert(13)
    bt.insert(3)
    bt.insert(10)

    print(bt.in_order())
    print(bt.pre_order())
    print(bt.post_order())