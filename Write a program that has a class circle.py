class circle():
    def __init__(self,radius,pi):
        self.radius= radius
        self.pi = pi
    def area(self):
        return self.pi* self.radius**2
    def circumference(self):
        return 2*self.pi*self.radius
r = int(input('Enter the radius--->>'))
A= circle(r,3.14)
print('The area of the circle-->',A.area())
print('The circumference of the circle-->',A.circumference())