L = [1,0,2,9,3,8,4,7,5,6]

def bubble_sort(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            L[i],L[i+1] = L[i+1],L[i]
        else:
            pass
        print(L)
bubble_sort(L)
