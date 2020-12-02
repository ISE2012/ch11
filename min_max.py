def min_max_tuple(t):
    """Returns the smallest and largest
    elements of a sequence as a tuple"""
    return (min(t), max(t), 10)

def min_max(t):
    """Returns the smallest and largest
    elements of a sequence as a tuple"""
    return min(t), max(t)

seq = [12, 98, 23, 74, 3, 54]

result = min_max_tuple(seq)
print(result)

# not in tuple form
result2 = min_max(seq)
print(result2)

min_value, max_value, mean_value = result
print("Min value:", min_value)
print("Max value:", max_value)

