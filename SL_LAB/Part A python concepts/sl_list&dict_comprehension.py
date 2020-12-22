#List comprehension
l1=[13,22,45,64,12,77,38,18]
l2=[i for i in l1 if i%2==0]
print("Output using list comprehension is",l2)


#Dictionary Comprehension
ld1=[2,3,5,6,8,10,13,17]
output_dict={}
for i in ld1:
    if i%2!=0:
        output_dict[i]=i**3
print(" Dictionary comprehension: ",output_dict)
