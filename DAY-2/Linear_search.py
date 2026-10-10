#Linear search
#Linear search is a searching alsorithm that checks each element in a collection sequentially until target is found

#Algorithm
#1.Start from the first element of array
#2.compare the current element with target value
#3.If the current element equals the target value
#4.Otherwise,move to the next element
#5.Repeat the comparisiion until the target is found or the array ends
#6.If the target is not found after checking every element,return -1

#code:
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=[10,20,40,60,30]
key=400
result=linear_search(arr,key)
if result !=-1:
    print("Element found at index:",result)
else:
    print("Element not found")