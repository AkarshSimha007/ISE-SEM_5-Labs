a=['ISE','CSE','MECH','CIVIL','EEE','ECE']

#printing values from index 1 to 3, 3 is not inclusive
print("Set of values:",a[1:3])

#printing using negative index
print("Negative Indexing:",a[-2])

#skipping alternate items
print("Alternate indexing:",a[0:-1:2])

#Printing item based on index
print("Index based printing:",a[2])

#Deleting an item
del a[2]
print("Remaining values after deleting",a)

#Inserting values At position
a.insert(3,"IEM")
print("Inserted list",a)

#reversing order of list
a.reverse()
print("Reversed order is:",a)

#Sorting the list
a.sort()
print("Sorted list is:",a)



