"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_stack(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

class Stack:
    def __init__(self):
        self.front = None
    
    def is_empty(self):
        return self.front == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.front
        self.front = new_node
    
    def pop(self):
        val = self.front.value
        save = self.front.next
        self.front.next = None
        self.front = save
        return val
    
    def peek(self):
        if(not self.front):
            return None
        return self.front.value
    
    # Create a new Stack
stack = Stack()

# Add elements to the stack
stack.push(('Educated', 'Tara Westover'))
stack.push(('Gone Girl', 'Gillian Flynn'))
stack.push(('Dune', 'Frank Herbert'))
print_stack(stack)

# View the front element
print("Peek: ", stack.peek()) 

# Remove elements from the stack
print("Pop: ", stack.pop()) 
print("Pop: ", stack.pop()) 

# Check if the stack is empty
print("Is Empty: ", stack.is_empty()) 

# Remove the last element
print("Pop: ", stack.pop()) 

# Check if the queue is empty
print("Is Empty:", stack.is_empty()) 
"""

import random

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def get_random(catalogue):
    store = []
    size = 0
    curr = catalogue
    while curr:
        store.append(curr.value)
        curr = curr.next
        size += 1
    random_number = random.randint(0, size-1)
    return store[random_number]
    
    


catalogue = Node(('Homegoing', 'Yaa Gyasi'), 
                Node(('Pachinko', 'Min Jin Lee'),
                         Node(('The Night Watchman', 'Louise Erdrich'))))

print(get_random(catalogue))