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


#Application of Linked list
# 1. Worst case insertion at the end and begin are O(1)
# 2. Worst case deletio from the beginning is O(1)
# 3. Insertion and deletion in the middle are O(1) if we 
# have reference to the previous node.
# 4. Round Robin Implementation
# 5. Merging two sorted linked list in faster than array
# 6. Implemenation of simple memory manager where we use
# need to link free blocks
# 7. Easier implementation of queue and deque data structure
# 
