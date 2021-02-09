#1Ba

# lst=[]
# noDup=[]

# def removeDup(l):
#     for i in l:
#         if i not in noDup:
#             noDup.append(i)
#     return noDup


# elestr=input("Enter list elements:")
# lst=elestr.split(" ")


# print(removeDup(lst))

# even=[]
# for i in noDup:
#     if(int(i)%2==0):
#         even.append(i)
# print(f"List of even numbers is {even}")

# ************************************************************

#1Bb

# from collections import Counter
# def wordCount(fname):
#     with open(fname) as f:
#         return Counter(f.read().split())
# print("Frequency of words is:\n",wordCount("sample.txt"))

# ************************************************************

#1Bc
def maxi(l):
    if len(l)==1:
        return l[0]
    else:
        m=maxi(l[1:])
        return m if m>l[0] else l[0]

elestr=input("Enter list elements:")
lst=elestr.split(" ")
nlst=[]
for i in lst:
    nlst.append(int(i))
print(lst)
print(nlst)
print(maxi(nlst))


