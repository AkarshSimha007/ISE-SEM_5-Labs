user_input=input("Enter the list items seperated by space")
user_list=user_input.split(" ")
user_list=[int(x) for x in user_list]
print(user_list)

even_list=[x for x in user_list if x%2==0]
print("List containing even numbers is",even_list)
print("\n\n*******Eleminating Duplicate elements*******")
o_list=[10,20,30,40,50,40,30,100,20]
new_list=set(o_list)
print(new_list)