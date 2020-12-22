d={1:'Amazon',2:'Flipkart',3:'Myntra',4:'Ajio'}
print(d)
print(d[1])
del d[4]
print(d)

print("Key value pairs:",d.items())
print("Keys of the dictionary:",d.keys())
print("Values of the dictionary:",d.values())
e=d.copy()
print("Shallow copy of the dictionary d:",e)
d.clear()
print("Trying to print the dictionary d:",d)
