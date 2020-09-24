import treenode

# Class representing a Binary Search Tree using TreeNodes        
class BinarySearchTree:
   
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = treenode.TreeNode(data)
        else:
            self._insert(data, self.root) 
            
    def _insert(self, data, curr_node):
        # If entry node < current node, add as left child if null, or recursively call method on left child if not null
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = treenode.TreeNode(data)
            else:
                self._insert(data, curr_node.left)
        # If entry node > current node, same as above but for right side of tree
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = treenode.TreeNode(data)
            else:
                self._insert(data, curr_node.right)
        # Otherwise value equals current tree node, and we do not add it to avoid duplicates
        else:
            print("Value is already present in BST")
            
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
    
    # Helper method recursively called in find() method    
    def _find(self, data, curr_node):
        # If != to desired value, repeat on left or right subtree depending on > or <. If ==, we have found the value
        if data > curr_node.data and curr_node.right:
            return self._find(data, curr_node.right)
        elif data < curr_node.data and curr_node.left:
            return self._find(data, curr_node.left)
        if data == curr_node.data:
            return True