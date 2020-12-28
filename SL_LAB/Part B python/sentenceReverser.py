class sentenceReverser:
    reverse=""
    sentence=""
    vowels=['a','e','i','o','u']
    vowelCount=0

    def __init__(self,sentence):
        self.sentence=sentence
        self.reverseSentence()

    def reverseSentence(self):
        self.reverse=" ".join(reversed(self.sentence.split()))

    def getVowelCount(self):
        self.vowelCount=sum(s in self.vowels for s in self.sentence.lower())
        return self.vowelCount

    def getReverse(self):
        return self.reverse

items=[]
print("Enter sentences below")
for i in range(3):
    sentence=input("Enter sentence:")
    reverser=sentenceReverser(sentence)
    items.append(reverser)
    print()

sortedItems=sorted(items,key=lambda item: item.getVowelCount(),reverse=True)

print("Sorted items in descending order of vowel count\n")
for i in range(len(sortedItems)):
    print("Reversed Sentence is:",sortedItems[i].getReverse(),",Vowel Count is:",sortedItems[i].getVowelCount())

