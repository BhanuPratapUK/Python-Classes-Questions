class ABC:
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
delattr(x,'val')