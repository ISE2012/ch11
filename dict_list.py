myList = [(5, 'candy'),(15, 'cookies'),(23, 'ice cream')] #key pairs list
myDict = dict(myList) # convert into dictionary
print("Type:", type(myDict))

print("print dictionary with for loop")
for key in myDict:
    print(key,"is",myDict[key])

