def helloworld():
 print("Hello World")

print("Simple Function:")
helloworld()

def greetUser(name):
 print(f"Hi {name} welcome to SL Lab")

print("Function with parameter")
name=input("Enter your name")
greetUser(name)

print("Function with default arguements")

def print_values(a,b=5):
 print(f"The values of a and b are {a} and {b}")

print_values(10,100)
