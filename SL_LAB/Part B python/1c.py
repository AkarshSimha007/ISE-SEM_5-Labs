def Max(list):
    if len(list)==1:
        return list[0]
    else:
        m=Max(list[1:])
        return m if m>list[0] else list[0]

def main():
    try:
        num_list=eval(input("Enter the listof numbers:"))
        print("the largest number is: ",Max(num_list))
    except SyntaxError:print("Enter comma seperated values")
    except:print("Enter numbers only")

main()
