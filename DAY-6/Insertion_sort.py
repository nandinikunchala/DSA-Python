#Insertion sort
#Insertion sort is a sorting algorithm that builds a sorted array one element at a time by taking an element &
#inserting it into its correct position among the elements on its left.

#Time complexity
#BC:o(n)-The array is already sorted, so the while loop condition fails immediately for each key.
#AC:o(n*2)-Elements typically need to be compared and shifted multiple times.
#WC:o(n*2)-In reverse order, each new key may need to be compared with and shifted past every preceding element.

#Space coomplexity
#auxiliary space:o(1)

#Algorithm
#1.Consider the first element as already sorted.
#2.Pick the next element(called key).
#3.Compare the key with elements on its left.
#4.Shift all larger elements one position to the right.
#5.Insert the key into its correct position.
#6.Move to the next element.
#7.Repeat until all elements are inserted into their correct position.

#code
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[5,3,4,2,1]
print(insertion_sort(arr))