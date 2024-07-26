'''


# we can use both methods to access the list of even and odd numbers

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





(10 question)class ABC:
    def __init__(self,val):
        self.val= val
    def display(self):
        print('The value is --<>',self.val)
x= ABC(1000)
x.display()
x.new1= 10
print(x.new1)
x.new2= 20
print(x.new2)
del x.new1
print(x.new2)
print(x.new1)


