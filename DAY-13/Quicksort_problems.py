#Write a Python program to sort arr = [8, 3, 5, 1, 9, 2] in ascending order using Quick Sort.
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[n//2]
    left=[]
    middle=[]
    right=[]
    for i in arr:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            middle.append(i)
        else:
            right.append(i)
    return quick_sort(left)+middle+quick_sort(right)
arr=[8,3,5,1,9,2]
print(quick_sort(arr))

#Write a Python program to sort arr = [15, 7, 20, 3, 10, 1] in descending order using Quick Sort.
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[n//2]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x>pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)
arr=[15, 7, 20, 3, 10, 1]
print(quick_sort(arr))

#Write a Python program to sort arr = [34, 12, 45, 2, 23, 8, 19] in ascending order using Quick Sort. Use the first element as the pivot.
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[0]
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
arr=[34, 12, 45, 2, 23, 8, 19]
print(quick_sort(arr))

#Write a Python program to sort arr = [50, 20, 70, 10, 40, 60, 30] in descending order using Quick Sort. Use the last element as the pivot.
def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[-1]
    left=[]
    middle=[]
    right=[]
    for x in arr:
        if x>pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)
        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right)
arr=[50, 20, 70, 10, 40, 60, 30]
print(quick_sort(arr))

