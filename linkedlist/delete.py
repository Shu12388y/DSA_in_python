class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.next = None




head = Node(10)
head.next = Node(15)
head.next.next = Node(20)



def delete(h:object):
    if h == None:
        return None 
    else:
        return h.next
    

delete(head)