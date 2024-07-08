class Node:
    def __init__(self,key):
        self.key = key 
        self.next = None


# Time complexity = O(n)
def main(h,i):
    if h == None:   # head is empty the insert the Node
        return Node(i)
    curr = h
    while curr.next != None:  # tranverse the linked list and find the end and then insert it
        curr = curr.next 
    curr.next = Node(i)
    return h         




head  =  Node(10)
head.next = Node(12)



if __name__ == "__main__":
    main(head,60)