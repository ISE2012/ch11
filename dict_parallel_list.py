names = ["Tina", "Pratik", "Amber"]
major = ["Social Work", "Pre-Med", "Art"]

major_dict = {}
for i in range(len(names)):
    key = names[i] # the key is the value from names list
    value = major[i] # the value is the value from major list
    major_dict[key] = value

print(major_dict)

