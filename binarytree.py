import treenode
import stack as s
import queue as q

# Class representing a Binary Tree using TreeNodes
class BinaryTree:
   
    def __init__(self, root):
        self.root = treenode.TreeNode(root)     
      
    # Helper function which helps determine which traversal order to traverse and print the tree
    def print_tree(self, traversal_order):
        if traversal_order == 'preorder':
            return self.preorder_print(self.root, "")   
        elif traversal_order == 'inorder':
            return self.inorder_print(self.root, "")
        elif traversal_order == 'postorder':
            return self.postorder_print(self.root, "")
        elif traversal_order == 'levelorder':
            return self.levelorder_print(self.root)
        elif traversal_order == 'reverselevelorder':
            return self.reverse_levelorder_print(self.root)
        
        else:
            print(f"Traversal type {traversal_order} is not supported") 
            return False
        
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + " - ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + ' - ')
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + " - ")
        return traversal
    
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = q.Queue()
        queue.enqueue(start)
        
        # While queue is not empty, print node at front of queue, and add its children to end of queue
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.front().data) + ' - '
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return
        
        queue = q.Queue()
        stack = s.Stack()
        queue.enqueue(start)
        
        # While queue not empty, add node at front of queue to stack, add its children to end of queue
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        # Unload the stack and print each value until the stack is empty        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.data) + ' - '
            
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
        
    def size(self):
        if self.root is None:
            return 0
        
        stack = s.Stack()
        stack.push(self.root)
        size = 1
        
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size
    
    def size_recursive(self, node):
        if node is None:
            return 0
        
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)
    
