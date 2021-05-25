import bst

def height(node):
    """each end node note as -1 for balance caculation"""
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    """def Nh = MAX(h(left), h(right)) + 1"""
    node.height = max(height(node.left), height(node.right)) + 1

class AVL(bst.BST):
    """
AVL binary search tree implementation.
Supports insert, find, and delete-min operations in O(lg n) time.
"""
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        """
        3 steps:
        1. x.right = y.left (with end node check)
        2. y.left = x 
        3. x.parent = y
        """
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        """
        3 steps:
        1. x.left = y.right 
        2. y.right = x 
        3. y.parent = x
        """
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)

    def insert(self, t):
        """Insert key t into this tree, modifying it in-place."""
        node = bst.BST.insert(self, t)
        self.rebalance(node)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def delete_min(self):
        node, parent = bst.BST.delete_min(self)
        self.rebalance(parent)
        #raise NotImplemented('AVL.delete_min')

def test(args = None):
    bst.test(args, BSTtype = AVL)

if __name__ == '__main__': test()



# AxBYc                   ==                      AxByC

        #             ---- Left Rotate --->>
        #     X                                       Y
        #    / \                                     /  \
        #   A   Y                                   X     C
        #      /  \                               /   \
        #     B     C                            A      B




        #             <<---- Right Rotate ---
        #     X                                       X
        #    / \                                     /  \
        #   A   Y                                   Y     C
        #      /  \                               /   \
        #     B     C                            A      B









