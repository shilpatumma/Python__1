# (1). Create a Tuple :

# thistuple = (1, 2, 3, 4)
# print(thistuple)

# thistuple = ("red", "orange", "pink", "yellow")
# print(thistuple)



# (2). Tuples allow duplicate values :

# thistuple = (1, 2, 3, 4, 2, 5, 3)
# print(thistuple)



# (3). Tuple Length :

# thistuple = (1, 2, 3, 4, 2, 5, 3)
# print(len(thistuple))



# (4). Create Tuple With One Item : (One item tuple, remember the comma:)

# thistuple = (1,)
# print(type(thistuple))

# thistuple = (1)
# print(type(thistuple))

# thistuple = ("red")
# print(type(thistuple))



# (5). Tuple Items - Data Types :

# thistuple1 = (1, 2, 3, 4)
# thistuple2 = ("red", "orange", "pink", "yellow")
# thistuple3 = (True, False)

# print(thistuple1)
# print(thistuple2)
# print(thistuple3)


# (6). A tuple with strings, integers and boolean values :

# tuple1 = ("abc", 34, True, 40, "flower")
# print(tuple1)



# (7). The tuple() Constructor :

# thistuple = (("apple", "cherry", "papaya"))
# print(thistuple)


# (8). Access Tuple Items :

# thistuple = (("apple", "cherry", "papaya"))
# print(thistuple[2])


# (9). Negative Indexing :

# thistuple = (("apple", "cherry", "papaya"))
# print(thistuple[-2])


# (10). Range of Indexes :

# thistuple = (("apple", "cherry", "papaya", "banana", "mango", "kiwi"))
# print(thistuple[2:6])


# (11). Range of Negative Indexes :

# thistuple = (("apple", "cherry", "papaya", "banana", "mango", "kiwi"))
# print(thistuple[-6:-4])


# (12). Check if Item Exists :

# fruit = (("apple", "cherry", "papaya", "banana"))
# if "papaya" in fruit:
#     print("Yes 'papaya' is in the fruit tupple")
# else:
#     print("No")


# fruit = (("apple", "cherry", "papaya", "banana"))
# if "kiwi" in fruit:
#     print("Yes 'kiwi' is in the fruit tupple")
# else:
#     print("No")



# (13). Python - Update Tuples : (Change Tuple Values)

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)


# num1 = (1, 2, 3, 4)
# num2 = list(num1)
# num2[1] = 100
# num1 = tuple(num2)

# print(num1)



# (14). Add Items : (append() method)

# 1. Convert into a list:

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = list(tuple1)
# tuple2.append(7)
# print(tuple2)


# 2. Add tuple to a tuple. 

# tuple1 = ("red", "orange", "pink", "blue")
# tuple2 = ("white",)
# tuple1 = tuple1 + tuple2
# print(tuple1)



# (15). Remove Items:

# tuple1 = ("red", "orange", "pink", "blue")
# tuple2 = list(tuple1)
# tuple2.remove("red")
# print(tuple2)



# (16). Python - Unpack Tuples : (Unpacking a tuple)

# fruits = ("apple", "banana", "cherry", "orange")

# (green, yellow, red, orange) = fruits

# print(green)
# print(yellow)
# print(red)
# print(orange)




# Using Asterisk* :

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)




# Add a list of values the "tropic" variable:

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)



# (17). Loop Through a Tuple :

# thistuple = ("red", "pink", "black")
# for x in thistuple:
#     print(x)


# (18). Loop Through the Index Numbers :

# thistuple = ("red", "pink", "black")
# for x in range (len(thistuple)):
#     print(thistuple[x])



# (19). Using a While Loop :

# tuple  = ["red", "orange", "yellow"]
# i = 0
# while(i < len(tuple)):
#     print(tuple[i])
#     i = i + 1



# (20). Python - Join Tuples : (Join Two Tuples)

# t1 = [1, 2, 3, 4]
# t2 = ["apple", "banana", "kiwi"]
# t3 = t1 + t2
# print(t3)



# (21). Multiply Tuples :

# colors = ["white", "green", "skyblue"]
# c1 = colors * 2
# print(c1)



# (22). Python - Tuple Methods : 

# (Python Tuple count() Method)
# n1 = [1, 2, 3, 4, 5, 9, 7, 9 ,9]
# n2 = n1.count(9)
# print(n2)


# Python Tuple index() Method

# n1 = [1, 2, 3, 4, 5, 9, 7, 9 ,9]
# n2 = n1.index(9)
# print(n2)