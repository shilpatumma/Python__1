# List Practice questions :
# (1). Creating a List:
# (a). Create a list of integers, strings, or a mix of both.

# integer_list = [1, 2, 3, 4, 5]

# string_list = ["apple", "banana", "cherry", "papaya"]

# mixed_list = [1, "apple", 2, "banana", 3, "cherry"]

# print(integer_list)
# print(string_list)
# print(mixed_list)



# (2). Accessing Elements:

# (a). Print the first and last elements of the list.
# (b). Print a specific element using its index.

# list = ["apple", "banana", "papaya", "kiwi", "cherry"]
# print(list[0], list[-1])

# list1 = [1, 2, 3, 4, 5]
# print(list1[2])




# (3). Slicing:

# (a). Print the first three elements of the list.
# (b). Print the last three elements of the list.

# thislist = ["red", "orange", "black", "pink", "white"]
# print(thislist[0:3])
# print(thislist[2:5])




# (4). Appending and Extending Lists:

# (a). Append a new item to the list.
# (b). Extend the list by adding another list to it.

# list = ["apple","banana","papaya"]
# list.append("kiwi")
# print(list)

# list1 = ["apple","banana","papaya"]
# list2 = ["red", "yellow", "orange"]
# list1.extend(list2)
# print(list1)



# (5). Inserting and Deleting Elements:

# (a). Insert a new element at a specific position in the list.
# (a). Delete an element from the list by its value or by its index.

# list = ["apple", "orange", "kiwi"]
# list.insert(2,"papaya")
# print(list)

# list = ["apple", "orange", "papaya", "kiwi"]
# list.remove("papaya")
# print(list)

# list = ["apple", "orange", "papaya", "kiwi"]
# list.pop(2)
# print(list)

# list = ["apple", "orange", "papaya", "kiwi", "mango"]
# del list[2]
# print(list)


# (6). List Operations:

# (a). Sort the list in ascending order.
# (b). Reverse the order of elements in the list.

# list = ["bananan", "watermelon", "muskmelon", "papaya"]
# list.sort()
# print(list)

# list = [19, 255, 301, 40, 99, 2]
# list.sort()
# print(list)


# list = ["banana", "watermelon", "muskmelon", "papaya"]
# list.sort(reverse = True)
# print(list)

# list = [19, 255, 301, 40, 99, 2]
# list.sort(reverse = True)
# print(list)




# (7). List Comprehension:

# (a). Create a new list by applying a transformation to each element 
#      of the original list using list comprehension.

# original_list = [1, 2, 3, 4, 5]
# squared_list = [x**2 for x in original_list]
# print(squared_list)




# (8). Iterating Over a List:

# (a). Use a for loop to print each element of the list.

# list = ["red", "pink", "blue"]
# for x in list:
#     print(x)



# (9). Checking Membership:

# (a). Check if a specific element exists in the list using the in keyword.

# list = [1, 2, 3, 4, 5, 6, 7, 8]
# if 4 in list:
#     print("Yes")
# else:
#     print("No")




# (10). List Length:

# (a). Print the length of the list.

# list = [1, 2, 3, 4, 5]
# print(len(list))






# Tuple Practice Questions : 

# (1). Creating and Accessing TuplesTask:

# Create a tuple with five cities you’d like to visit.
# Access the second and fourth city in the tuple.
# Try changing the first city to another city and observe the result.

# Ans...

# cities = ("Surat", "Mumbai", "Ahmedabad", "Vapi", "Valsad")
# print(cities)

# print(cities[1])
# print(cities[3])

# c1 = list(cities)
# c1[0] = "Baroda"
# cities = tuple(c1)
# print(cities)




# (2). Task: Count how many times a particular city appears in the tuple.
# Find the index of a specific city in the tuple.

# Ans...

# cities = ("Surat", "Mumbai", "Ahmedabad", "Vapi", "Valsad")
# for x in range (len(cities)):
#     print(x)

# cities = ("Surat", "Mumbai", "Ahmedabad", "Vapi", "Valsad")
# c2 = cities.count("Surat")
# print(c2)




# (3). Task: Unpack the tuple into individual variables.
# Create a tuple of tuples and access nested elements.

# Ans...

# tuple = (1, 2, 3, 4, 5)

# (one, two, three, four, five) = tuple
# print(one)
# print(two)
# print(three)
# print(four)
# print(five)


# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3) 






# Set Practice Questions : 


# (1). Creating and Manipulating Sets Task: 

# Create a set of unique colors. 
# Add a new color to the set.
# Remove a color from The set

# Ans...

# colors = {"Red", "Yellow", "Pink", "Black", "Blue"}
# print(colors)

# colors2 = {"White", "Orange"}
# colors.update(colors2)
# print(colors)

# colors.remove("Pink")
# print(colors)




# (2). Task: Create another set of colors and find the union and intersection of both sets.
# Check if a color is in the set
# Convert a list with duplicate colors into a set to remove duplicates.

# Ans...

# color1 = {"Red", "Yellow", "Blue", "Pink"}
# color2 = {"Black", "Blue", "White"}

# color3 = color1.union(color2)
# print(color3)

# color3 = color1.intersection(color2)
# print(color3)



# color1 = {"Red", "Yellow", "Blue", "Pink"}
# if "Yellow" in color1:
#     print("YES")
# else:
#     print("NO")



# thislist = ["Red", "Yellow", "Blue", "Pink", "Yellow"]
# thisset = set(thislist)  
# print(thisset)






# Dictionary Practice Question : 

# (1). Creating and Accessing DictionariesTask :

# Create a dictionary with three key-value pairs representing a student’s grades.
# Access the grade for a specific subject.
# Add a new subject and grade to the dictionary.
# Update the grade for an existing subject.

# Ans...

# dict = {
#     "Gujarati" : 90,
#     "Hindi" : 98,
#     "English" : 91
# }
# print(dict)
# print(dict["Hindi"])


# dict = {
#     "Gujarati" : 90,
#     "Hindi" : 98,
#     "English" : 91
# }
# dict["computer"] = 94
# print(dict)
# dict["Hindi"] = 84
# print(dict)




# (2). ask: Use a for loop to print each subject and its corresponding grade.
# Use GET to safely retrieve the grade for a subject that might not exist.
# Remove a subject from the dictionary.

# Ans...

# dict = {
#     "Gujarati" : 90, 
#     "Hindi" : 98,
#     "English" : 91
# }
# print(dict)

# for x, y in dict.items():
#     print(x , y)


# dict.pop("English")
# print(dict)





# (1). Find the size of a set in python.
# Ans...

# set = {"Car", "Bus", "Scooty", "Bike"}
# print(len(set))



# (2). Iterate over a set in python.
# Ans...

# set = {"Car", "Bus", "Scooty", "Bike"}
# for i in set:
#     print(i)


# (3). Pyton - Maximum and Minimum in set.
# Ans...

# set = {1, 2, 98, 6, 66, 0}
# list = list(set)

# maximum = max(list)
# minimum = min(list)

# print("Maximum", maximum)
# print("Minimum", minimum)



# (4). Python - remove items from set.
# Ans...

# set = {"red", "orange", "blue", "pink", "white"}
# set.remove("orange")
# print(set)



# (5). Python - Check if two lists have at-least one element common
# Ans...

# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]
# set1 = set(list1)
# set2 = set(list2)

# set3 = set1.intersection(set2)
# print(set3)



# (6). Python program to find common elements in three lists using sets.
# Ans...

# list1 = ["apple", "kiwi", "orange", "banana"]
# list2 = ["apple", "cherry", "orange", "banana"]
# list3 = ["banana", "orange", "kiwi", "cherry"]
# set1 = set(list1)
# set2 = set(list2)
# set3 = set(list3)

# set4 = set1.intersection(set2).intersection(set3)
# print(set4)



# (7). Python Find missing and additional values in two lists.
# Ans...

# list1 = ["a", "b", "c", "d", "e"] 
# list2 = ["d", "e", "f", "g"]

# missing_values = set(list1).difference(list2)
# additional_values = set(list2).difference(list1)

# print("Missing values :",missing_values)
# print("Additional values :",additional_values)



# (8). Python program to find the diffrence between two lists.
# Ans...

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# difference1 = list(set(list1) - set(list2))
# print(difference1)

# difference2 = list(set(list2) - set(list1))
# print(difference2)



# (9). Python set difference to find lost element from a duplicated array
# Ans...

# array1 = {1, 2, 3, 4, 5}
# array2 = {2, 3, 4, 5, 6}

# array3 = array1.difference(array2)
# print(array3)



# (10). Python program to count number of vowels using sets in given string 
# Ans...

# string = str(input("\nEnter a string : "))
# print(string)
# count  = 0
# vowels = "aeiouAEIOU"

# for alphabet in string:
#     if alphabet in vowels:
#         count +=1

# print("Count number of vowels :",count)


# (11). Concatenated string with uncommon characters in Python
# Ans...

# str1 = "java"
# str2 = "javascript"

# print(str1)
# print(str2)

# Uncommon_char = set(str1).symmetric_difference(str2)
# print(Uncommon_char)



# (12). Python - program to accept the strings which contains all vowels.
# Ans...

# l = input("Input a letter of the alphabet: ")

# if l in ('a', 'e', 'i', 'o', 'u'):
#     print("%s is a vowel." % l)

# else:
#     print("%s is a consonant." % l)



# (13). Python - Check if given string is binary or not.
# Ans...

# str = input("\nEnter the binary string  : ")
# flag = True

# for char in str:
#     if(char == "0" or char == "1"):
#         continue
#     else:
#         flag = False
#         print("The string is not a binary string")
#         break
# if(flag):
#     print("The string is a binary string")



#(14). Python - set to check if string is panagram
# Ans...

# string = "The quick brown fox jumps over the lazy dog"

# alphabet = set('abcdefghijklmnopqrstuvwxyz')

# string_set = set(char.lower() for char in string if char.isalpha())

# is_pangram = alphabet == string_set
# print(is_pangram)



# (15). Python - set pairs of complete strings in two sets
# Ans...

# set1 = {1, 2, 3}
# set2 = {"a", "b", "c"}

# pairs = {(x, y) for x in set1 for y in set2}
# print(set1)
# print(set2)
# print(pairs)



# (16). Python program to check whether a string is heterogram or not
# Ans...

















# (1). Cretae a list of all divisables of 5 or 7 in the range 0 to 1000.
# then create another list by filtering the previous list based on divisables of 3 & 4.

# Ans...


# strating_range = int(input("Enter the strating range : "))
# ending_range = int(input("Enter the ending range : "))

# for i in range (strating_range, ending_range + 1):
#     if(i % 7== 0 and i % 5 == 0):
#         print(i)

# new_list1 = int(input("Enetr the starting number : "))
# new_list2 = int(input("Enetr the ending number : "))

# for i in range (new_list1, new_list2 + 1): 
#     if(i % 3 == 0 and i % 4 == 0):
#         print(i)




# (2). create a dictionary with the key 1 to 100 & has value of it's square.
# then create a tuple by maping key value of it by following formula. (key*3/value + 4)

# Ans...

# square_dictionary = dict()
# for x in range(1,101):
#     # print(x)
#     square_dictionary[x] = x*x
#     print(x)
#     print(square_dictionary[x])




# (3). Create a dictionary with the key 0 to 20 & values must be factorials of those keys.
# then map this dictionary by values which are square root of value.
# use math-sqrt()method for square root.

# Ans...

# for i in range(1,21):
#     print(i)

# num = int(input("\nEnter a number : "))
# factorial = i = 1
# if num >= 1:
#     for i in range (1, num + 1):
#         factorial = factorial * i
# print("Factorial of the given number is :",factorial)