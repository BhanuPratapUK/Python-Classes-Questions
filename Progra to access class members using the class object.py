class ABC():
    var = 100
    def show(self):
        print("Hey how are you I am inside of this class Methods")
display = ABC()
print('The value of the var is-->',display.var)
display.show()