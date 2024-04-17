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
####print#################################################
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
####reverse the whole linklist#################################################
            
def reverse(head):
    prev,next = None, None
    current= head
    
    while current:
        next = current.next  # if current is null it gives you error for current.next so first check current the assign current.next
        current.next = prev
        prev = current
        current= next
    head = prev    
    return head            
input_linked_list = LinkedList()
input_linked_list.create_linked_list([1, 2, 3, 4, 5]) 
print_list_with_forward_arrow(reverse(input_linked_list.head)) 
      
####reverse in group######################################
def reverse_linked_list(head,k):
    prev,next = None, None
    current= head
    
    for _ in range(k):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev, current    
        

def reverse_group(head,k):
 
    dummy = LinkedListNode(0)
    dummy.next = head
    ptr = dummy
    while ptr :
        
        tracker = ptr
        for _ in range(k):
            
            if tracker == None:
                 break
            tracker = tracker.next
        if tracker == None:
                 break
        prev,current = reverse_linked_list(head,k)         
        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = prev
        ptr = last_node_of_reversed_group
           
    return dummy.next           
input_linked_list = LinkedList()
input_linked_list.create_linked_list([1, 2, 3, 4, 5]) 
print_list_with_forward_arrow(reverse_group(input_linked_list.head,3)) 