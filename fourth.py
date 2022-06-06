# Dictionary is nothing but key value pairs
d1 = {"mohit": "pizza", "nandini": "dairy milk", "sujal": "berger", "bank": {"A": "rupees", "B": "office", "C": "person"}}
                        # it describe the dictionary.
# print(type(d1))       # it prints the datatype of function.
d1["abc"] = "extra"     # it inserts the item in dictionary.
print(d1)               # it prints the hole dictionary.
print(d1["mohit"])      # it prints the value of mohit from the dictionary.
print(d1["bank"]["A"])  # it prints the value (d1-->bank-->A) from the dictionary.
"""del d1["bank"]["A"]     # it deletes the value (d1-->bank-->A) from the dictionary.
print(d1)"""
d2 = d1.copy()          # it copied the dictionary.
del d2["abc"]           # it deletes the item from the copied d2 dictionary.
print(d2)
print(d1)
d2["xyz"] = "brother"
print(d2)
print(d2.keys())        # it prints all the keys from the dictionary.
print(d2.items())       # it prints all the items from the dictionary.
print(len(d2))          # it prints the length of the dictionary.
