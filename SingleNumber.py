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




(9 questions)def scale(x):
    return x*10
class ABC:
    def __init__(self,var):
        self.var = var
    def display(self):
        print('The value is-->',self.var)
    def modify(self):
        self.var = scale(self.var)
x = ABC(3)
x.display()
x.modify()
x.display()
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
(11 Question)class ABC:
    def __init__(self,val):
        self.val= val
    def display(self):
        print('The value is --<>',self.val)
x= ABC(1000)
x.display()
print('Checking the value is present or not-->',hasattr(x,'val'))
getattr(x,'val')
setattr(x,'val',12)
print('The value is present in or not-->',x.val)
delattr(x,'val')'''

