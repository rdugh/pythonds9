class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, key):
        if self.left_child is None:
            self.left_child = BinaryTree(key)
        else:  # if there IS a left child
            t = BinaryTree(key)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, key):
        if self.right_child is None:
            self.right_child = BinaryTree(key)
        else:  # if there IS a right child
            t = BinaryTree(key)
            t.right_child = self.right_child
            self.right_child = t
            
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def get_root_val(self):
        return self.key
    
    def set_root_val(self, new_key):
        self.key = new_key
    
    def __repr__(self):
        return f"BinaryTree({self.key!r})"
