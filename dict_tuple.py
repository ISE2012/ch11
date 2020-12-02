dict_dt = {'a':10, 'b':1, 'c':22}
list_tuples = list(dict_dt.items()) #dictionary to list of tuples
print(list_tuples)

for key, value in list_tuples:
    print(key, value)

