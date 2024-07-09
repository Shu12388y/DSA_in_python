class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.next = None



def deleteLast(h:object):
    if h == None:
        return None
    if h.next == None:
        return None
    curr  =  h 
    while curr.next.next != None:       # find the second last node
        curr = curr.next
    curr.next = None
    return h 


head = Node(10)
head.next = Node(16)


deleteLast(head)