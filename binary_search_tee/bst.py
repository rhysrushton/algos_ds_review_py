class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(new_val, self.root)
    
    def insert_helper(self, new_val, place):
        if new_val < place:
            if place.left:
                self.insert_helper(new_val, place.left)
            else:
                place.left = Node(new_val)
        else:
            if root.right:
                self.insert_helper(new_val, place.right)
            else:
                place.right = Node(new_val)
                
                
        

    def search(self, find_val):
        return self.search_helper(find_val, self.root)
    
    def search_helper(self,find_val, root):
        if root:
            if find_val == root.value:
                return True
            else:
                if find_val < root.value:
                    self.search_helper(find_val, root.left)
                else:
                    self.search_helper(find_val, root.right)
        
        return False
        
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print( tree.search(4))
# Should be False
print( tree.search(6))