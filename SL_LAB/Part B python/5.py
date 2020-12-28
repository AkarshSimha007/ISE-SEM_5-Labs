import os
import sys
from functools import reduce

dict={}

if(len(sys.argv)!=2):
    print("Invalid Arguments")
    sys.exit()

if(not(os.path.exists(sys.argv[0]))):
    print("File does not Exist!")
    sys.exit()

if(sys.argv[1].split(".")[-1]!="txt"):
    print("Invalid file format, only .txt files are allowed")

with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
            dict[word]=dict.get(word,0)+1

sortedDict=sorted(dict.items(),key=lambda sortedI:sortedI[1],reverse=True)
for i in range(len(sortedDict)):
    print(sortedDict[i])

wordlen=[]

for i in range(10):
    try:
        wordTuple=sortedDict[i]
        print("\nWord Tuple is:",wordTuple)
        wordlen.append(len(wordTuple[0]))
        print(wordTuple[0],",Frequency:",wordTuple[1],",Length of word:",len(wordTuple[0]))
    except IndexError:
        print("File conains less than 10 words")

print("Length of 10 top occuring words:",wordlen)

sum=reduce(lambda x,y:x+y,wordlen)
print("Average length is:",sum/len(wordlen))
