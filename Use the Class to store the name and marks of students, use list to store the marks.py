class student():
    def __init__(self,name):
        self.name= name
        self.marks = []
    def entry(self):
        for i in range(3):
            mark = int(input('Enter the marks of subject %d-->'%(i+1)))
            self.marks.append(mark)
    def print(self):
        print('Here is the name of the person',self.name)
        print('Here is the marks in the subject->',self.marks)
A = student('Bhanu')
A.entry()
B = student('Shiv')
B.entry()
A.print()
B.print()

