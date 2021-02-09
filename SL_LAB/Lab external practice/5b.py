import sys
import os
from functools import reduce

if(len(sys.argv)!=2):
    print("Invalid Arguements")
    sys.exit()

if(not(os.path.exists(sys.argv[0]))):
    print("Invalid File Path!")
    sys.exit()

if(sys.argv[1].split(".")[-1]!="txt"):
    print("Invalid File Format!")
    sys.exit()

dict={}

with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
            dict[word]=dict.get(word,0)+1

sortedDic=sorted(dict.items(),key=lambda item: item[1],reverse=True)
wordLen=[]

for i in range(10):
    try:
        wordTuple=sortedDic[i]
        print("Word tuple is",wordTuple)
        wordLen.append(len(wordTuple[0]))
        print("Length of word is",wordLen[i])
    except IndexError:
        print("File does not have more than 10 words")
print(wordLen)
sum=reduce(lambda x,y: x+y,wordLen)
print("Average Word Length is",sum/len(wordLen))

squares=[x**2 for x in wordLen if x%2!=0]
print(squares)