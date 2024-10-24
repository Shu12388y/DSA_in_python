# n -> number of pages
# p -> target page
def page(n, p):
    pages = [(0, 1)]  # Starting with a pair (0, 1)
    temp1 = 0
    temp2 = 0
    
    # Generating pages as pairs (i, i+1)
    for i in range(2, n+1, 2):
        pages.append((i, i + 1))
    
    print("Pages:", pages)
    
    # Counting from start (forward loop)
    for i in range(0, len(pages)):  # Use full range of pages list
        if pages[i][0] != p and pages[i][1] != p:
            temp1 += 1
        else:
            break  # Stop as soon as p is found
    
    print("Steps from start (temp1):", temp1)
    
    # Counting from end (reversed loop)
    for i in reversed(range(0, len(pages))):
        if pages[i][0] != p and pages[i][1] != p:
            temp2 += 1
        else:
            break  # Stop as soon as p is found
    
    print("Steps from end (temp2):", temp2)
    
    # Finding the minimum steps
    minPage = min(temp1, temp2)
    print("Minimum steps to reach page:", minPage)

# Example check
page(6, 1)



def Second(n,p):
   if(n%2==0 and p==n-1 and p!=1):
       return 1 
   if((p//2)+1>(n-p)//2):
       return (n-p)//2
   else:
       return p//2