#Sort the array [29, 10, 14, 37, 13] using Selection Sort.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
arr=[29,10,14,37,13]
print(selection_sort(arr))

#Write a Python program to sort arr = [29, 10, 14] in ascending order using Selection Sort.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
arr=[29,10,14]
print(selection_sort(arr))

#Write a Python program to sort arr = [45, 12, 30, 8, 25] in descending order using Selection Sort.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        max_idx=i
        for j in range(i+1,n):
            if arr[j]>arr[max_idx]:
                max_idx=j
        arr[i],arr[max_idx]=arr[max_idx],arr[i]
    return arr
arr=[45,12,30,8,25]
print(selection_sort(arr))

#Write a Python program to sort arr = [64, 25, 12, 22, 11, 90] in ascending order using Selection Sort.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
arr=[64,25,12,22,11,90]
print(selection_sort(arr))