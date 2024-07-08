class Node:
    def __init__(self,key) -> None:
        self.key = key 
        self.next = None



# insert at beginning
def insert(h,i):
    temp  = Node(i)   # making a new node
    temp.next = h     # pointing to the head
    # tranvser the list 
    while  temp != None:
        print(temp.key)
        temp  = temp.next


    




# Linked list implementation
head = Node(10)
head.next = Node(15)



insert(head,90)



