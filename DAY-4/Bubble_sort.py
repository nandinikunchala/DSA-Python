#Bubble sort
#Bubble sort is the sorting algorithm that arranges elements in ascending or descending order by comparing adjacent elements 
#and swapping them when they are in the wrong order

#Algorithm
#1.Start with first element.
#2.Compare the first and second elements.
#3.If the first element is greater than the second,swap them.
#4.Move to the next pair of adjacent elements.
#5.Continue until the end of the array.
#6.After the first pass,the largest element reaches the end.
#7.Repeat the process for remaining unsorted elements.
#8.Stop when the array is sorted.

#code
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[5,3,8,2,1]
result=bubble_sort(arr)
print(result)