class Node:
    def __init__(self,key):
        self.key = key 
        self.next = None




# Time complexity is O(n)
def main(h):
    cur  = h 
    while cur != None:
        print(cur.key)
        cur = cur.next





head = Node(10)
head.next = Node(20)
head.next.next = Node(15)



if __name__ == "__main__":
    main(head)