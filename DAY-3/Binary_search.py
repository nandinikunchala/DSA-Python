#Binary search
#Binary search is a searching algorithm that finds an element in a sorted array by repeatedly dividing the search space into
#two halves
#Binary search uses three important variables:low,high and mid
#low-represents the index of the first element in current search range
#high-represents the index of last element in current search range
#mid-represents the index of the middle element in the current search range

#Algorithm
#1.Initialize low and high.
#low=0
#high=n-1
#2.Calculate the middle index.
#mid=(low+high)//2
#3.Check whether the midddle element is the target.
#4.If both are equal,return the index
#5.If the target is greater than the middle element:
#search the right half
#update low=mid+1
#6.If the target is smaller than the middle element:
#search the left half
#update high=mid-1
#7.Repeat until the element is fnd or low>high
#8.If not found,return -1

#Time complexity
#BC:o(1)
#AC:o(log n)
#WC:o(log n)

#Space complexity
#auxilary space:o(1)

#code:
def binary_search(arr,key):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[10,20,30,40,50,60,70]
key=60
result=binary_search(arr,key)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found")