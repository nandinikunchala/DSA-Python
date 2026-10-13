#Selection sort
#Selection sort is a sorting algorithm that repeatedly finds the smallest element from the unsorted part of an 
#array and swaps it with the first element of that unsorted part.

#Time complexity
#BC:o(n*2)-even an already sorted array requires comparision
#AC:o(n*2)-the algorithm checks the remaining elements in every pass
#WC:o(n*2)-It still performs a quadratic no.of comparisions

#Algorithm
#1.Assume the first element is the minimum.
#2.Compare it with all remaining elements.
#3.Find the smallest element in the unsorted part.
#4.Swap the smallest element with the first unsorted position.
#5.Move the boundary of the sorted part by one position.
#6.Repeat for the remaining unsorted elements.
#7.Contnue until the entire array becomes sorted.

#code:
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
arr=[30,2,20,5,10]
print(selection_sort(arr))