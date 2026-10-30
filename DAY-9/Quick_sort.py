#Quick sort
#Quick Sort is a sorting algorithm that uses the Divide and Conquer technique to sort elements in ascending or descending order.
#It picks a pivot element and partitions 
#the array into two — elements smaller than pivot and greater than pivot — then sorts them recursively.

#Time complexity:
#Best case:O(n log n)
#Average case:O(n log n)
#Worst case:O(n*2)

#Space complexity:
#Average space complexity:O(n)
#Worst-case space complexity:O(n)

#Algorithm
#1.Select a pivot element
#2.Partition the array into:
#            Elements smaller than pivot
#            pivot element
#            Elements greater than pivot
#3.Recursively apply quick sort on left partition
#4.Recursively apply quick sort on right partition
#5.Combine the sorted left partition,pivot and sorted right partition
#6.Continue until all partitions contain one or zero elements

##code:
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[n//2]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)
a=[8,6,4,9,1,2]
print(quick_sort(a))