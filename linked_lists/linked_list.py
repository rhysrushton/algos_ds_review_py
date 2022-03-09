##the below is an implementation of a linked list in python with explanation of how it works. 


##we are defining a class for an element in a linked list. 
class Element(object):
    #init initializes a new element. 
    #the element has a value associated with it. 
    #the element also has a variable the points to the next element in the linked list.
    def __init__(self, value):
        self.value = value
        self.next = None

# we now set up the linked list class. 
#it has a head which we will populate with an Element when constructing the linked list. 
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

#We have a method on the LinkedList Object. 
#This method takes a new_element and adds it to the LinkedList class

    def append(self, new_element):
        #set variable current equal to the first element in the linked list.
        #remember that if there is no head then it will be equal to null. 
        current = self.head
        #now if the linked list has a head i.e. self.head != None
        #then we will loop through the list and add elements. 
        if self.head:
        #then while there is a non-null value linked to the current element loop through the list
        #once you get to a null value then assign the new element to that null
            while current.next:
                current = current.next
            current.next = new_element
        #if the linked list is empyt then just
        #populate the linked list witht he new element. 
        else:
            self.head = new_element


############Udemy Exercise
"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
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
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current_node = self.head
        current_position = 1
        
        if self.head == None:
            return None
        while current_node:
            if current_position == position:
                return current_node
            elif current_position != position: 
                current_node = current_node.next
                current_position += 1
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current_node = self.head
        previous = current_node
        next = current_node.next
        current_position = 1
        if position == 1: 
            new_element.next = current_node
            return
        while current_node:
            if position == current_position:
                previous.next = new_element
                new_element.next = current_node
                return
            
            previous = current_node
            current_node = current_node.next
            current_position += 1
            

    def delete(self, value):
        """Delete the first node with a given value."""
        current_node = self.head
        previous = None
        if value == current_node.value:
            self.head = current_node.next
            current_node = None
            
            return
        while current_node: 
            if current_node.value == value: 
                previous.next = current_node.next
                current_node = None
                
                return 
            
            previous = current_node
            current_node = current_node.next
            


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)

#alternatove deletion method. 
def delete(self, value):
    current = self.head
    previous = None
    while current.value != value and current.next:
        previous = current
        current = current.next
    if current.value == value:
        if previous:
            previous.next = current.next
        else:
            self.head = current.next