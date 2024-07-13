class Number:
    even = []
    odd = []
    def __init__(self,val):
        self.val = val
        if val%2==0:
            Number.even.append(val)
        else:
            Number.odd.append(val)
    # def display(self):
    #     print('The list of the even numbers -->',number.even)
    #     print('Ths list of the odd number is-->',number.odd)

x = Number(2)
x1 = Number(3)
x2 = Number(4)
x3 = Number(5)
print('The list of the even numbers -->',Number.even)
print('Ths list of the odd number is-->',Number.odd)