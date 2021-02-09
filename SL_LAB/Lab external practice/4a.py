class Student:
    name=""
    age=0
    sublist=[]

    def __init__(self,name,age,l):
        self.name=name
        self.age=age
        self.sublist=l

    def accept(self):
        self.name=input("Enter Student name:")
        self.age=int(input("Enter age:"))
        l=input("Enter marks in three subjects:")
        l=l.split(" ")
        x=[]
        for i in l:
            x.append(int(i))
        self.sublist=x

    def display(self):
        print(self.name)
        print(self.age)
        print(self.sublist)

s1=Student("Akarsh",20,[99,92,90])
s1.display()

s2=Student("Bp",20,[89,92,96])
s2.display()
s2.accept()
s2.display()