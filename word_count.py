file_data = open('romeo-full.txt')
counts = dict()
for line in file_data:
    line = line.lower() # lowercase
    words = line.split() # get each word
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    tuple_data = (val, key)
    lst.append(tuple_data)

# sort the list from higher to lower
lst.sort(reverse=True)
print("Min:", min(lst))
print("Max:", max(lst))

for key, val in lst[:10]: # get top 10
    print(key, val)
    
    
    