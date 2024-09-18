L = [1,3,5,6,8,9,0]

def binary_Search(item):
    median = len(L//2)
    for i in range(L):
        if item<median:
            return i
        elif item>median:
            return i
        else:
            return i[len(L//2)]
        
binary_Search(8)
