import matplotlib.pyplot as plt


class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.inorder_pos = 0

    def add(self, key):
        if key < self.key:
            if self.left:
                self.left.add(key)
            else:
                self.left = TreeNode(key)
        elif key > self.key:
            if self.right:
                self.right.add(key)
            else:
                self.right = TreeNode(key)

    def remove(self, key):
        # traverse recursively until key is found
        if key < self.key:
            if self.left:
                self.left = self.left.remove(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.remove(key)
        else:

            x = self

            # set parent reference if node is a leaf node
            if not self.left and not self.right:
                return None

            # determine which direction child of the removed node is in and set parent reference to removed parent
            # reference
            elif self.left and not self.right or self.right and not self.left:
                if not self.left:
                    return self.right
                else:
                    return self.left

            # node to remove has two branches of children
            elif self.left and self.right:
                # find node with largest key among the left branch
                y = self.left
                while y.right:
                    y = y.right

                # save the max key and then remove y
                x.key = y.key
                x.left = x.left.remove(y.key)
        return self

    def inorder(self, num, key_list):
        """
        Parameters
        ----------
        num: list
            List of a single element which keeps
            track of the number I'm at
        """
        if self.left:
            self.left.inorder(num, key_list)
        self.inorder_pos = num[0]
        key_list.append(self.key)
        num[0] += 1
        if self.right:
            self.right.inorder(num, key_list)

    def draw(self, x):
        y = self.inorder_pos
        plt.scatter([x], [y], 50, 'k')
        plt.text(x + 0.2, y, "{}".format(self.key))
        x_next = x + 1
        if self.left:
            y_next = self.left.inorder_pos
            plt.plot([x, x_next], [y, y_next])
            self.left.draw(x_next)
        if self.right:
            y_next = self.right.inorder_pos
            plt.plot([x, x_next], [y, y_next])
            self.right.draw(x_next)


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def inorder(self):
        key_list = []
        if self.root:
            self.root.inorder([0], key_list)
        return key_list

    def remove(self, key):
        if self.root:
            self.root = self.root.remove(key)

    def draw(self):
        self.inorder()
        if self.root:
            self.root.draw(0)

    def add(self, key):
        if self.root:
            self.root.add(key)
        else:
            self.root = TreeNode(key)


def make_tree():
    T = BinaryTree()
    for val in [10, 7, 16, 3, 9, 11, 20, 14, 17, 13, 12, 6, 5, 17, 15, 8, 4]:
        T.add(val)
    return T

'''######################################################################################'''

class dfs_node:
    def __init__(self):
        self.edges = []
        self.index = None
        self.neighbor = []
        self.on_fire = False
        self.burnt = False
        
        
def dfs(node):
    stack = [node]
    node.on_fire = True
    while len(stack) > 0:
        node = stack.pop()
        node.burnt = True
        for n in node.edges:
            if not n.on_fire:
                n.on_fire = True
                stack.push(n)
    
