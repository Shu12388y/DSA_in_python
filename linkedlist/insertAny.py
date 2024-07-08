class Node:
    def __init__(self,key) -> None:
        self.key = key
        self.next = None



# T.C = O(min(pos,n))  n--> lenght of the linked list
def main(h:object,i:int,pos:int):
    temp = Node(i)
    if pos == 1:
        temp.next = h 
        return temp 
    curr = h 
    for i in range(pos-2):
        curr = curr.next
        if  curr == None:
            return h 
    temp.next = curr.next
    curr.next = temp 
    return h    




head = Node(10)
head.next = Node(12)
head.next.next = Node(32)



if __name__ == "__main__":
    print(main(head,12,3))