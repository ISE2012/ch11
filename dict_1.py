dict1 = {"first_name" : "John", "last_name" : "Cleese"}

# accesed key from dictionary
fname = dict1["first_name"]
print("First name is", fname)

#using for loop to iterate over dictionary
print("using for loop to iterate over dictionary:")
for key in dict1:
    # key is the key inside the dict1 dictionary
    print(key,"is",dict1[key])


