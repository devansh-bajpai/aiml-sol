ls = [60, 20, 40, 10, 90, 30, 80, 50]

def merge_sort(ls):
    mid = len(ls)//2
    if (len(ls) <= 1):
        return ls
    leftHalf = ls[:mid]
    rightHalf = ls[mid:]
    leftHalf = merge_sort(leftHalf)
    rightHalf = merge_sort(rightHalf)
    return merge(leftHalf, rightHalf)

def merge(leftHalf, rightHalf):
    i, j = 0, 0
    new = []
    while(i< len(leftHalf) and j<len(rightHalf)):
        if (leftHalf[i] < rightHalf[j]):
            new.append(leftHalf[i])
            i += 1
        else:
            new.append(rightHalf[j])
            j += 1
        
    new.extend(leftHalf[i:])
    new.extend(rightHalf[j:])
    return new

print(merge_sort(ls))