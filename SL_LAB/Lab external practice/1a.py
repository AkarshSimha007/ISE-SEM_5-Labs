lst=[]
n=input("Enter number of elements:")
for i in range(int(n)):
    ele=int(input())
    lst.append(ele)

print(lst)
print(f"{max(lst)} is the maximum")
print(f"{min(lst)} is the minimum")

newele=int(input("Enter an element to be inserted:"))
lst.append(newele)
print(lst)

delele=int(input("Enter element to be deleted:"))
if delele in lst:
    lst.remove(delele)
else:print("Element not found!")
