class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None



def removeDuplicate(head:object)->None:
    curr = head 
    while curr != None and curr.next != None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next 
        else:
            curr = curr.next 


head = Node(12)
head.next = Node(13)
head.next.next = Node(15)




def main():
    removeDuplicate(head)


if __name__ == "__main__":
    main()

