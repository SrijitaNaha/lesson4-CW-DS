arr = [12,15,7,8,9,10]
num = 7

def linear_search(arr,num):
    c = -1
    for i in range(len(arr)):
        if arr[i] == num:
            return i   
    return c

result = linear_search(arr,num)
if result == -1:
    print(f"{num} not found in the list")
else:
    print(f"{num} found at index {result}")