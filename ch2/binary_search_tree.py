

class Node:
    
    # define node init 
    def __init__(self, data):
        self.left = None 
        self.right = None
        self.data = data
        
    # insert into tree
    def insert(self, data):
        # if provide data exist 
        if self.data:
            # 1 check to left child
            # compare with parent node
            if data < self.data:
                # 1.1 if left child not yet exist 
                if self.left is None:
                    self.left = Node(data)
                # 1.2 if left child exist, insert to the next level(child)
                else:
                    self.left.insert(data)
            # 2 check to right child
            # compare with parent node 
            elif data > self.data:
                # 2.1 if right child not yet exist 
                if self.right is None:
                    self.right = Node(data)
                # 2.2 if right child exist, insert to the next level(child)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
        
        
    # print func
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()



root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.print_tree()
