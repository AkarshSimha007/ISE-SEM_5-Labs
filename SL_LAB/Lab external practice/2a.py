class Rectangle:
    def __init__(self):
        self.l=int(input("Enter Length:"))
        self.b=int(input("Enter Breadth:"))

    def area(self):
        print("Area of rectangle is:",self.l*self.b)

r=Rectangle()
r.area()
        