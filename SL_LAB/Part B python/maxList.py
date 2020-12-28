def Max(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        m=Max(numlist[1:])
        return m if m>numlist[0] else list[0]

def main():
        num_list=eval(input("Enter a list of numbers:"))
        print("The largest number is:",Max(num_list))


main()
 