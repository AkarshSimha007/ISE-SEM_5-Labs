from functools import reduce
num=[2,4,6,8,10,12]
lst=[x*3 for x in num]
print(lst)

org_sum=reduce(lambda x,y: x+y,num)
print("Original sum is:",org_sum)

new_sum=reduce(lambda x,y:x+y,lst)
print("New sum is:",new_sum)