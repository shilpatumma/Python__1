# (1). List :

# thislist = ["apple", "banana", "cherry"]
# print(thislist)


# (2). Allow Duplicates :

# thislist = ["apple", "banana", "cherry", "apple",]
# print(thislist)


# (3). List length :
# thislist = ["apple", "banana", "cherry", "mango"]
# print(len(thislist))



# (4).List items - Data types :
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 2, 3, 4]
# list3 = [True, False, True]

# print(list1)
# print(list2)
# print(list3)


# list1 = ["apple", 2, "banana", True, 3, "cherry"]
# print(list1)



# (5). type() :
# thislist = ["apple", "banana", "cherry", "apple"]
# print(type(thislist))


# (6). List Constructor() :
# thislist = list(("apple", "banana", "cherry"))
# print(thislist)


# (7). Access List items :
# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# print(thislist[4])


# (8). Negative indexing :
# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# print(thislist[-3])


# (9). range of indexes :
# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# print(thislist[1:3])

# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# print(thislist[:3])

# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# print(thislist[2:])



# (10). range of negative indexes :
# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# print(thislist[-4:-1])



# (11). Check if item exists :  (using (in) keyword)
# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# if "apple" in thislist:
#     print("yes, 'apple', is in the fruit list")


# thislist = ["apple", "banana", "cherry", "watermelon", "mango"]
# if "papaya" in thislist:
#     print("yes, 'apple', is in the fruit list")
# else:
#     print("NO")



# (12). Python - Change List Items  (Change Item Value) :
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "papaya"
# print(thislist)



# (13). Change a Range of Item Values :
# thislist = ["apple", "banana", "cherry", "papaya", "watermelon", "blackcurrent"]
# thislist[1:4] = "kiwi", "mango", "muskmelon"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "papaya"]
# thislist[2:3] = "kiwi", "mango", "muskmelon"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "papaya"]
# thislist[1:3] = "kiwi", "mango"
# print(thislist)



# (14). Insert items :
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1,"papaya")
# print(thislist)



# (15). Python - Add List Items :  (Append Items)
# thislist = ["apple", "banana", "cherry"]
# thislist.append("papaya")
# print(thislist)


# (16). Extend List :
# thislist1 = ["apple", "banana", "cherry"]
# thislist2 = ["papaya", "kiwi", "mango"]
# thislist1.extend(thislist2)
# print(thislist1)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)



# (17). Add Any Iterable :
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)



# (18). Remove List Items - (Remove Specified Item) :
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("cherry")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "mango", "papaya", "cherry"]
# thislist.remove("cherry")
# print(thislist)


# (19). Remove Specified Index :
# thislist = ["apple", "banana", "cherry", "mango"]
# thislist.pop(2)
# print(thislist)

# thislist = ["apple", "banana", "cherry","mango"]
# thislist.pop()
# print(thislist)


# del keyword
# thislist = ["apple", "banana", "cherry", "mango"]
# del thislist[2]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "mango"]
# del thislist
# print(thislist)


# (20). Clear the List :
# thislist = ["apple", "banana", "cherry", "mango"]
# thislist.clear()
# print(thislist)


# (21). Loop Lists :
# thislist = ["apple", "banana", "cherry", "mango"]
# for x in thislist:
#     print(x)


# (22). Loop Through the Index Numbers :
# thislist = ["apple", "banana", "cherry", "mango"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist = ["apple", "banana", "cherry", "mango", "papaya"]
# for i in range(len(thislist)):
#     print(i)


# (23). Using a While Loop :
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while (i < len(thislist)):
#     print(thislist[i])
#     i = i +1



