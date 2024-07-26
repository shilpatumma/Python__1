# (1). Python Sets :
# A set is a collection which is unordered, unchangeable*, and unindexed.

# thisset = {"apple", "banana", "kiwi"}
# print(thisset)


# Duplicate values : 

# thisset = {"apple", "banana", "apple", "kiwi", "apple", "apple"}
# print(thisset) 


# True and 1 : considered as same value.

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)



# False and 0 : considered as same value.

# thisset = {"apple", "banana", "cherry", False, 0, 2}
# print(thisset) 



# (2). Get the Length of a Set :

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))



# (3).Set Items - Data Types : (String, int and boolean data types:)

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}

# print(set1)
# print(set2)
# print(set3)


# A set with strings, integers and boolean values:

# set1 = {"abc", False, 1, "NAme"}
# print(set1)



# (3).type() :
# set1 = {"rose", "lotus", "jasmine"}
# print(type(set1))


# (4). The set() Constructor :

# set1 = (("rose", "lotus", "jasmine"))
# print(set1)



# (5). Python - Access Set Items :

# thisset = {"apple", "kiwi", "papaya"}
# for x in thisset:
#     print(x)


# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)



# (6). Python - Add Set Items :

# set = {"apple", "guava", "pineapple"}
# set.add("kiwi")
# print(set)



# (7). Add Sets :

# s1 = {"apple", "orange", "kiwi"}
# s2 ={"guava", "pineapple", "papaya"}
# s1.update(s2)
# print(s1)


# (8). Python - Remove Set Items :

# remove() method :

# s1 = {"apple", "orange", "kiwi"}
# s1.remove("kiwi")
# print(s1)


# discard() method :

# s1 = {"apple", "orange", "kiwi"}
# s1.discard("kiwi")
# print(s1)


# pop() method :

# s1 = {"apple", "orange", "kiwi"}
# x = s1.pop()
# print(x)
# print(s1)


# clear() method :

# s1 = {"apple", "orange", "kiwi"}
# s1.clear()
# print(s1)



# del keyword :

# s1 = {"apple", "orange", "kiwi"}
# del s1
# print(s1)




# (9). Python - Loop Sets :

# set = {"apple", "banana", "papaya"}
# for x in set:
#     print(x)




# (10). Python - Join Sets :

# union() method

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# s3 = s1.union(s2)
# print(s3)



# | operator instead of the union() method, 

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# s3 = s1 | (s2)
# print(s3)



# JoinMiltiple Sets :

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# s3 = {7, 8, 9}
# s4 = (10, 11, 12)
# s5 = s1.union(s2, s3, s4)
# print(s5)


# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# myset = set1 | set2 | set3 |set4
# print(myset)


# (11). Join a Set and a Tuple :

# a = {1, 2, 3}
# b = (4, 5, 6)
# c = a.union(b)
# print(c)



# (12). Update() method :

# s1 = {1, 2, 3}
# s2 = {8, 9, 4}
# s1.update(s2)
# print(s1)



# (13). Intersection :

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# print(set3)


# ou can use the & operator instead of the intersection() method, 
# and you will get the same result.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)



# (14). The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.intersection_update(set2)

# print(set1)




# (15). The values True and 1 are considered the same value. 
# The same goes for False and 0.

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set3 = set1.intersection(set2)

# print(set3)



# (16). difference() method :

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)  



# (17). You can use the - operator instead of the difference() method, 
# and you will get the same result. :

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)



# (18). difference_update() method :

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)



# (19). symmetric_difference() method :

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)

# print(set3)



# (20).You can use the ^ operator instead of the symmetric_difference() method, 
# and you will get the same result.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)




# (21). symmetric_difference_update() method:

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)