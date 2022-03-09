"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

#the below shows how to implement a stack and also how to perform various operation on it. 
#our stack is going to be comprised of a linked list, meaning the elements within the stack are going to 
#be the elements in a linked list, but because our linked list are within the stack we essentially only ever access the head of the linked list.
#if we want to add we have to add to the head and if we want to remove we have to remove the head first. 

#creating a node type element for our linked list. 
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

 #this is the class for our linked list
 # notice the two methods insert_first and delete_first
 # This enables us to have stack type functionality built in to the linked list        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

# create our stack object. 
class Stack(object):
    def __init__(self,top=None):
        #this is an important line to understand
        # in this function we initialise the stack object. 
        # when we intialise the stack we create an attribute which is equal to the linked list class
        # we initialise the linked list class with an Element.
        self.ll = LinkedList(top)
    
    #here we can use linked list methods. 
    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
     

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)