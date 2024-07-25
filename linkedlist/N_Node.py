# Find the Nth Node from the end of the linked list

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


# ---------  Method 1 ----------
def findNode(n:int,head):
    h = head
    count = 0  
    while h:
        h = h.next
        count += 1
    if count < n:
        print("")
    h = head         
    for _ in range(1,count-n+1):
        h = h.next
        print(h.data)


# ---------- Method 2 ------------------


# 1. Move 'First' Pointer n position ahead
# 2. Start 'Second' Pointer from head
# 3. Move both the pointer at same speed. When the first pointer reached 'Null' second pointer reaches the required Node.

def twoPointer(n:int,head:object):
    if head == None:
        return 
    first = head 
    for i in range(1,n):
        if first == None:
            return
        first = first.next
    second = head 
    while first != None:
        second = second.next 
        first = first.next
    print(second.data) 



def main():
    findNode()



if __name__ == "__main__":
    main()
