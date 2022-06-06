# list in python
# list is just like as an array

things = ["clothes", "bottle", "lunchbox", "dinner table", "anything", "45", "82.45"]
print(things[6])
# index = [0, 1,  2, 3,  4,  5, ]
numbers = [8, 6, 55, 44, 99, 257,]
# numbers.sort()    # numbers sort in ascending order
# numbers.reverse()  # numbers sort in descending order but first use upper statement
numbers.append(23)  # it adds a number in the list in the last
print(numbers)
# syntax = numbers.insert(index,value)
numbers.insert(2, 48)     # it adds a number after index 2
print(numbers)
numbers.remove(48)      # it removes the value from the list
numbers.pop()           # it deletes the last element from the list
print(numbers)
numbers[1] = 33         # it changes the value of index
print(numbers)
# syntax = print(numbers[index:length])
print(numbers[0:4])  # it prints the array or list upt0 index 4
print(numbers[::2])  # it skipped the 1 value then print the array
print(max(numbers))   # it prints the maximum value number from the list.
print(min(numbers))   # it prints the minimum value number from the list.
del numbers[2]       # it deletes the value from the list
print(numbers)
