# delete node using pointer address no head pointer is given

class Node:
    def __init__(self,key) -> None:
        self.key = key 
        self.next = None 




def deleteRandom(ptr):
    tmp = ptr.next               # ptr is the given address store the address in tmp
    ptr.data = tmp.data          # store the data of tmp in ptr
    ptr.next = tmp.next          # now point the ptr to tmp.next
        