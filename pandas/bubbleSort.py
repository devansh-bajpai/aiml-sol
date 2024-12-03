ls = [20, 24,5,9,1,0,95]
def bubble(ls):
    for i in range(len(ls)):
        swapped = False
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                swapped = True
        if not swapped:
            break
    return ls

print(bubble(ls))