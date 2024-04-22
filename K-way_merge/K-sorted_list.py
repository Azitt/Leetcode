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
            
###k-sorted list###################################
from heapq import *
def merge_2_lists(head1,head2):
    
    dummy = LinkedListNode(0)
    prev = dummy

    while head1 and head2:
     
      if head1.data < head2.data:
          prev.next = head1
          head1 = head1.next
      else: 
          prev.next = head2
          head2 = head2.next 
      prev = prev.next
    if head1 is not None:
        prev.next = head1
    else:
        prev.next = head2          
    return dummy.next  
      
list1 = LinkedList()
list1.create_linked_list([2, 4, 6, 8]) 
list2 = LinkedList()
list2.create_linked_list([1, 3, 5, 7]) 
print_list_with_forward_arrow(merge_2_lists(list1.head,list2.head))            