def cf(c):
    return ((9/5)*c+32)

def fc(f):
    return (5/9*(f-32))

def ck(c):
    return c+273.15

def kc(k):
    return k-273.15

def fk(f):
    return ck(fc(f))

def kf(k):
    return cf(kc(k))

op1=[]
op2=[]
op3=[]
op4=[]
op5=[]
op6=[]

select='y'

while(select=="y" or select=="Y"):
    ch=0
    print("1.C->F,2.F->C,3.C->K,4.K->C,5.F->K,6.K->F")
   
    ch=int(input("Enter your choice:"))
    
    if(ch==1):
        c=float(input("Enter temperature in celcius:"))
        op1.append([c,cf(c)])
        print("Celsius to Farenhiet\n")
        print(sorted(op1))

    elif(ch==2):
        f=float(input("Enter temperature in Farenheit:"))
        op2.append([f,fc(f)])
        print("Farenhiet to Celcius\n")
        print(sorted(op2))

    elif(ch==3):
        c=float(input("Enter temperature in celcius:"))
        op3.append([c,ck(c)])
        print("Celsius to Kelvin\n")
        print(sorted(op3))

    elif(ch==4):
        k=float(input("Enter temperature in kelvin:"))
        op3.append([k,kc(k)])
        print("Kelvin to Celsius\n")
        print(sorted(op4))

    elif(ch==5):
        f=float(input("Enter temperature in farenheit:"))
        op3.append([f,fk(f)])
        print("Farenheit to Kelvin\n")
        print(sorted(op5))

    elif(ch==6):
        k=float(input("Enter temperature in Kelvin:"))
        op3.append([k,kf(k)])
        print("Kelvin to Farenheit\n")
        print(sorted(op6))

    else:print("Invalid Input!")

    select=input("Enter y to continue or n to terminate:")




