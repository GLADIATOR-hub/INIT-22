
    
def countingSort(arr, exp1):
 
    n = len(arr)
 
   
    output = [0] * (n)
 
   
    count = [0] * (10)
 
    
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1
 
    
    for i in range(1, 10):
        count[i] += count[i - 1]
 
   
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
 
   
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
 
 
# Driver code
arr = []
 
# number of elements as input
n = int(input("Enter number of elements for the radix or counting sort list : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele) # adding the element
     
print(arr)
 
# Function Call
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i])
print("The above list is sorted using the radix or counting sort technique")
    
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
 
 
# Driver code
arr = []
 
# number of elements as input
n = int(input("Enter number of elements forthe heap sort list : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    arr.append(ele) # adding the element
     
print(arr)
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])
print("The above list is sorted using heap sort technique")
