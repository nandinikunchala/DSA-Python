#1.Find the index of 30.
# arr = [10, 20, 30, 40, 50]
# key = 30
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[10,20,30,40,50]
key=30
result=linear_search(arr,key)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found")

#2.Find 25 in the list.
# arr = [10, 20, 30, 40]
# key = 25
def linear(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[10,20,30,40]
key=25
result=linear(arr,key)
if result!=-1:
    print("Element found at index:",result)
else:
    print("Element not found")

#3.Find the index of 5.
# arr = [5, 10, 15, 20]
# key = 5
def linear(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[5,10,15,20]
key=5
result=linear(arr,key)
if result!=-1:
    print(result)
else:
    print("Element not found.")

#4.Given arr = [10, 20, 30, 40, 50], find the index of target = 40 using Linear Search.
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[10,20,30,40,50]
key=40
result=linear_search(arr,key)
if result!=-1:
    print(result)
else:
    print("Element not found.")