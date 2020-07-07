mytuple=('cherry',"berrries","pineapple")
print(mytuple)
#print the value of a tuple

# print(mytuple[1])

#Tuples can be iterarted over a loop

# for x in mytuple:
#     print(x)


##Negavtive indexing

# print(mytuple[-1])

#try changing the values of a tuple

''' Once you created a tuple you cant change the values or modify the values '''
''' Yes we know that we cant add values to the tuple, but i want elements to be added to the tuple'''
# step1 : create a tuple with set of values
# mytuple=('cherry',"berrries","pineapple")
#
# #step2: covert them into a list
#
# mylist=list(mytuple)
#
# #step3:add elemenst to the new list
# mylist.append("Watermelon")
# mylist.append("PineApple")
# mylist.append("JackFruit")
#
# #ste4: convert the new list into tuple
# mytuple=tuple(mylist)
#
# print(type(mytuple))
# print(mytuple)


'''check for the element existance'''

# if "cherry" in mytuple:
#     print("true")
# else:
#     print("False")

''' get the length of tuple'''

# print(len(mytuple))
''' As we dont have privelages to add the element to the tuple, we can not remove the elements also'''

''' count and index'''
print(mytuple.index("pineapple"))
