#Merge sort
#Merge sort is a sorting algorithm that uses the divide and conquer technique.It works in three main steps:
#1.Divide-divide the array into small halves
#2.Sort-Keep dividing until each subarray contains only one element
#3.Merge-combine the smaller subarrays in sorted order until the entire array is sorted

#Time complexity
#BC:o(n log n)
#AC:o(n log n)
#WC:o(n log n)

#Space complexity
#auxiliary space:o(n)

#Algorithm
#1.Divide the array into two equal halves.
#2.Recursively divide each half until each subarray contains only one element.
#3.Merge two sorted subarrays into a single sorted array.
#4.compare elements from both subarrays while merging.
#5.Place the smaller element into the merged array.
#6.Continue until all elements are merged.
#7.Repeat merging until the complete sorted array is formed.

#code
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
arr=[38,27,43,10,7]
merge_sort(arr)
print(arr)

