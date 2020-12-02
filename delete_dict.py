dict1 = {'FName': 'Mike', 'LName': 'Jones', 'Age': 18}

print("Before Update")
print("dict1['FName']: ", dict1['FName'])
print("dict1['LName']: ", dict1['LName'])
print("dict1['Age']: ", dict1['Age'])


del dict1['FName'] # remove entry with key 'Name'
#dict1.clear()     # remove all entries in dict
#del dict1         # delete entire dictionary

print("After Update")
print("dict1['LName']: ", dict1['LName'])
print("dict1['Age']: ", dict1['Age'])
