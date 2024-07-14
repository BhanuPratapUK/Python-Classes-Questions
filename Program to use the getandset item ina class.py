class number:
    def __init__(self,list1):
        self.list1 = list1
    def __getitem__(self,index):
        return self.lis1[index]
    def __setitem__(self,index,value):
        self.list1[index] = value
A = number([11,12,1,31,41,45,66])
print(A.list1)
print(A.list1[5])
A[3]= 100000
print(A.list1)