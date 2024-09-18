L = [1,0,2,9,3,8,4,7,5,6]

def selection_Sort(L):
    for i in range(len(L)-1):
        first_index = 0
        for j in range(len(L)-1):
            if L[i]<=L[j]:
                pass
            else:
                L[i] , L[j] = L[j] , L[i]
        print(L)
selection_Sort(L)