class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.next = None 


def insertionSort(h:object,x:int):
    temp = Node(x)
    if h == None:
        return temp 
    elif x < h.key:
        temp.next = h
        return temp
    else:
        curr = h 
        while curr.next != None and curr.next.key < x:
            curr = curr.next 
        temp.next = curr.next
        curr.next = temp
        return h
    


head = Node(10)
head.next = Node(30)


print(insertionSort(head,15))