class number:
    var = 0
    def __init__(self,num):
        self.num= num
        number.var +=1
        print(self.num)
        print(number.var)
    def __del__(self):
    
        print('Here is %i is deleted'% self.num)

x = number(10)
y = number(20)
z = number(30)

del x
print(y.num)
print(z.num)