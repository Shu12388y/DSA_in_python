class Node:
    def __init__(self,key):
        self.key=key
        self.next=None



# Time complexity is O(n)
def main(h,x):
    cur = h
    while cur != None:
        if cur.key == x:
            print(cur.key)
            break
        else:
            cur = cur.next    
    else:
        print("Not found")            

head = Node(10)
head.next = Node(15)
head.next.next = Node(40)





if __name__ == "__main__":
    main(head,150)