import node

# Implementation of Linked List data structure using the Node class above   
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        
    def append(self, data):
        new_node = node.Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def prepend(self, data):
        new_node = node.Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert(self, data, after_val):
        '''Data is value you want to add to your LL, after_val is the value of the node that will point to new node '''
        new_node = node.Node(data)
        curr_node = self.head
        # Find the node which will precede the new node
        try:
            while curr_node.data != after_val:
                curr_node = curr_node.next
        except AttributeError:
            print("Previous node not in the LinkedList")
            return
        # Insert new node by pointing to next node of the preceding node, then have previous node point to it   
        new_node.next = curr_node.next
        curr_node.next = new_node
        
    def delete_node(self, data):
        curr_node = self.head
        # Case of deleting the head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            return
        
        # Otherwise find node with data (raise exception if doesn't exist)
        prev = None
        try:
            while curr_node.data != data:
                prev = curr_node
                curr_node = curr_node.next
        except AttributeError:
            print("Desired node not in the LinkedList")
            return
        # Remove the found node from the list by pointing previous node around it to next node
        prev.next = curr_node.next
        curr_node.next = None
        
    def delete_at_position(self, pos):
        curr_node = self.head
        # Case of deleting the head node
        if curr_node and pos == 0:
            self.head = curr_node.next
            curr_node = None
            return

        # Iterate through nodes until reaching desired index
        index = 0
        prev = None
        while curr_node and index != pos:
            prev = curr_node
            curr_node = curr_node.next
            index += 1
        # Case of index being larger than length of LL   
        if curr_node is None:
            print("Position is greater than length of LinkedList")
            return 
        # Delete the node if found
        prev.next = curr_node.next
        curr_node.next = None  
        
    def length(self):
        curr_node = self.head
        count = 0
        
        while curr_node:
            count += 1 
            curr_node = curr_node.next
            
        return count
    
    def swap_nodes(self, k1, k2):
        # If both inpout values are the same, no swap required
        if k1 == k2:
            return 
        
        # Set pointers to two nodes with desired swap values and the nodes which point to them
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != k1:
            prev_1 = curr_1
            curr_1 = curr_1.next
            
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != k2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        # If either value not found in LL, cannot proceed with swap operation    
        if not curr_1 or not curr_2:
            print("At least one of the input elements not present in LinkedList")
            return
        # If nodes have previous nodes (i.e. they are not heads), have previous respective nodes point to the other node 
        # If one of the nodes to be swapped is a head node, make the other node the head instead
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
            
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        # Swap the pointers of the nodes    
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def reverse_iterative(self):
        # For each node starting at head, have pointer for current next node ('nxt'), change node to point to its previous node, current node
        # becomes previous node for the following node, move to following node to reverse it
        prev = None
        curr_node = self.head
        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = nxt
        # Make previous tail the new head
        self.head = prev
        
    def reverse_recursive(self):
        # Helper function which recursively calls itself to perform reverse operation on each node
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
           
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)
        # Begin call to helper starting with current head of the LL
        self.head = _reverse_recursive(curr=self.head, prev=None)
         
    def remove_duplicates(self):
        curr = self.head
        prev = None
        # If current node data exists in dictionary, delete it. Else it is 1st occurence, add data to dictionary
        duplicates = dict()
        while curr:
            if curr.data in duplicates:
                prev.next = curr.next
                curr = None
            else:
                duplicates[curr.data] = 1
                prev = curr   
            curr = prev.next
            
    def merge(self, llist):
        # Set pointers to the head of each list
        p = self.head
        q = llist.head
        
        # Null cases
        if not p:
            return q
        if not q:
            return p
        
        # If we have two non-empty linked lists
        if p and q:
            #If list p's node smaller than q's set s to p, otherwise set s to q since q is smaller
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s == q
                q = s.next
            # Head of ordered list will be the node we determined above
            new_head = s
        # While p and q still have nodes remaining...
        while p and q:
            # If p smaller than q, next node is this smaller value in p, move s to this value, move p to its next node 
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next  
            # Otherwise q is smaller, so we point to the node in q, then update q to its next node (and s follows behind)
            else:
                s.next = q
                s = q
                q = s.next
        # IF reach end of either list, append the remaining nodes of the other list to the end of merged list
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def nth_to_last(self, n):
        curr = self.head
        index = 0
        while self.length() - n != index:
            curr = curr.next
            index += 1
        return curr.data
    
