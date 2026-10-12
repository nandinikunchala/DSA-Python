#Bubble sort
#Bubble sort is the sorting algorithm that arranges elements in ascending or descending order by comparing adjacent elements 
#and swapping them when they are in the wrong order.

#Bubble Sort is a comparison-based sorting algorithm that repeatedly compares adjacent elements
#and swaps them if they are in the wrong order until the array is sorted.

#Time complexity
#BC:o(n*2)[the given code performs all its comparision even array is already sorted]
#AC:o(n*2)[elements generally require multiple comparisions and swaps]
#WC:o(n*2)[A reverse-sorted array requires many swaps]

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