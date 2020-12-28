from functools import reduce
dict={}
wordlen=[]
with open("sample.txt") as f:
    for line in f:
        for word in line.split(" "):
            dict[word]=dict.get(word,0)+1

sortedDict = sorted(dict.items(), key=lambda dictI: dictI[1], reverse=True)
print("\n\n***********Top 10***********\n\n")
top_10=[]
lengths=[]
for i in range(10):
    top_10.append(sortedDict[i])
    print(top_10[i])
print()

#wordlen is a list of lists containing the top 10 words along with their lengths
#lengths is a list containing the lengths of the top 10 words
for i in top_10:
    wordlen.append([i[0],len(i[0])])
    lengths.append(len(i[0]))
print(wordlen)

sum=reduce(lambda x,y:x+y,lengths)
print(sum)
print(sum/len(lengths))

squares=[x**2 for x in lengths if x%2==0]
print(squares)