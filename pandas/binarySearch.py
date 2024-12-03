myArr = [1, 2, 4, 7, 9, 14, 34, 65, 90]
target = 65

def binary(arr, target):
    left, right = 0, len(arr) - 1

    while(left <= right):
        mid = (left+right)//2

        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary(myArr, 5))