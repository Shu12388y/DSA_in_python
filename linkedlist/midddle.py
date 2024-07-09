class Node:
    def __init__(self,key) -> None:
        self.key = key 
        self.next = None



def MiddleNode(h:object):
    curr  = h
    count = 0 
    while curr:
        curr = curr.next
        count += 1
    curr  = h
    for i in range(count//2):
        curr = curr.next
    print(curr.key)


head = Node(10)
head.next = Node(13)
head.next.next  = Node(20)
head.next.next.next = Node(30)


MiddleNode(head)





# --------------------- solution 2 ----------------------


# using fast and slow pointer

def twoPpinter(h):
    if h == None:
        return None 
    slow = h
    fast = h 
    while fast  != None and fast.next is not None:
        slow =  slow.next
        fast =  fast.next.next 
    print(slow.key)


twoPpinter(head)

