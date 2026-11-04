#Write a Python program to sort arr = [8, 3, 5, 1, 9, 2] in ascending order using Bubble Sort.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[8,3,5,1,9,2]
print(bubble_sort(arr))

#Write a Python program to sort arr = [12, 4, 7, 2, 15, 6, 1] in descending order using Bubble Sort.
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[12, 4, 7, 2, 15, 6, 1]
print(bubble_sort(arr))

#Sort [35, 12, 25, 8, 18] using Bubble Sort in ascending order.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[35,12,25,8,18]
print(bubble_sort(arr))

#Sort [64, 25, 12, 22, 11, 90] in ascending order.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[64,25,12,22,11,90]
print(bubble_sort(arr))

#Sort [50, 20, 40, 10, 30] using Bubble Sort in ascending order
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[50,20,40,10,30]
print(bubble_sort(arr))

#Sort [75, 15, 60, 5, 45, 30] using Bubble Sort in descending order.
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[75,15,60,5,45,30]
print(bubble_sort(arr))
