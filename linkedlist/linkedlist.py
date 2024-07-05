# Implement Node using class named Node 

class Node:
    def __init__(self,k):
        self.key = k 
        self.next = None



temp1 = Node(12)
temp2 = Node(22)
temp1.next = temp2 
head = temp1


print(temp1.next)



