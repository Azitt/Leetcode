class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#####LinkedList###################################################

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None
    
    def get_length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count    
    
    # insert_node_at_head method will insert a LinkedListNode at 
    # head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method. 
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""        
####print#################################################################
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")
            

      
##swap kth nodes###########################################
def swap_nodes(head,k):
 
    current, end = head, None
    
    count = 0
    while current: 
        count += 1
        if count == k:
            front = current
            end = head
        elif count >k: 
            end = end.next   
        current = current.next
                    
    front.data, end.data = end.data, front.data

           
    return head           
input_linked_list = LinkedList()
input_linked_list.create_linked_list([7, 4, 6, 1, 5,8]) 
print_list_with_forward_arrow(swap_nodes(input_linked_list.head,2)) 

##swap pairs###########################################
def swap_nodes_pairs(head):
 
    dummy = LinkedListNode(0)
    dummy.next = head
    prev = dummy
    
    while prev.next and prev.next.next:
        
        first = prev.next 
        second = prev.next.next
        # Swapping
        first.next = second.next
        second.next = first
        prev.next = second

        # Move to the next pair
        prev = prev.next.next      
        
    return dummy.next           
input_linked_list = LinkedList()
input_linked_list.create_linked_list([7, 4, 6, 1, 5,8]) 
print_list_with_forward_arrow(swap_nodes_pairs(input_linked_list.head)) 

