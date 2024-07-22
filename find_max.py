def find_max(arr, n):
    max = arr[0]
    for i in range (1,n):
        if arr[i]>max:
            max=arr[i]
    return max

arr = [10,20,30,1,80,8]
n = len(arr)
ans = find_max(arr,n)
print("Largest element in array :",ans)               