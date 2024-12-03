class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(25)
node4 = Node(69)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = node1

# Printing the linked list
while current is not None:
    print(current.data, end="-->")
    current = current.next
print(None)


node5 = Node(74) # Creating new node to be added

# Adding node5 at the end
while current.next is not None:
    current = current.next

current.next = node5
current = head

while current is not None:
    print(current.data, end= '-->')
    current = current.next
print(None)



# Inserting at specific position
while (current is not None and current.data != 20):
    current = current.next

node5.next = current.next
current.next = node5


current = head
while(current is not None):
    print(current.data, end='-->')
    current = current.next