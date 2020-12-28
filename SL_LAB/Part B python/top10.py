from collections import Counter
f=open("sample.txt","r")
contents=f.read()
words=contents.split(" ")
Counter=Counter(words)
top_10=Counter.most_common(10)
print(top_10)
print(top_10[1][0])
word_len=tuple([len(x[0]) for x in top_10])
print(word_len)
print(sum(word_len)/len(word_len))