"""list1 = [["harry","1"], ["mohit","2"], ["mayank","3"], ["nandini","4"], ["sujal","5"]]
dict1 = dict(list1)
for a in dict1.items():
    print(a)"""
list2 = [int, float, "double", 45, 6, 78, 5, 2, 3]
for item in list2:
    if str(item).isnumeric() and item>5:
        print(item)