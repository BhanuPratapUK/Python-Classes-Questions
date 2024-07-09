class Number:
    even = 0
    def cross_check(self,val):
        if val%2==0:
            self.even=1
    def even_odd(self,val):
        self.cross_check(val)
        if self.even==1:
            print('This Number  is even ')
        else:
            print('This is Number is ODD')
x =Number()
x.even_odd(21)