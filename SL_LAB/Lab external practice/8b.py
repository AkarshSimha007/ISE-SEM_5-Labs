class sentenceReverser:
    vowels=['a','e','i','o','u']
    vowelCount=0
    sentence=""
    reverse=""

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

for i in range(3):
    sentence=input("Enter a Phrase:")
    reverser=sentenceReverser(sentence)
    items.append(reverser)
    print()

sortedList=sorted(items,key=lambda item:item.getVowelCount(),reverse=True)

print("Reversed and vowel count is")

for i in range(len(sortedList)):
    print("Reversed Sentence is:",sortedList[i].getReverse(),",Vowel Count is:",sortedList[i].getVowelCount())
    