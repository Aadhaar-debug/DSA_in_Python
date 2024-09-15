class MyLimitedList:
    def __init__(self):
         self._L = []
    def append(self, item):
         self._L.append(item)
         print(self._L)
    def __getitem__(self, index):
         return self._L[index]
    
M = MyLimitedList()
M.append(200)
M.append(100)
print(M.__getitem__(1))
