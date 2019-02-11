# Our friend, the List
import random

my_list = ["Bev", "Abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_nums = [8, 4, 7, 5, 2, 9]

print (my_list[1])# print Abe
print (my_list[4:])# print Eve, Flo, and Gus
print(my_list[:3]) # print Bev, Abe, Cam as ['Bev', 'Abe', 'Cam']
print (my_list[2:4]) # print Cam and Dan
print(my_list[-2]) # count back from the end, print Flo

# copy of a list
#my_list2 = my_list don't do it this way!
my_list2 = my_list[:] # makes a copy, do it this way
my_list2.append("Hal") # add Hal to the end
print(my_list2)
print(my_list)

# if in
if "Cam" in my_list:
    print("Cam is in there. He's in there real good. Oh yeah Cam. Stay in there. Nice.")

# 2d list
my_list2d = [["Bev", 8], ["Abe", 12], ["Cam", 4]] # make a list with two elements. here we have kids and their names
print(my_list2d[1][0]) # target the second list ([["Abe", 12]) and the first item ("Abe")
print(my_list2d[-1]) # last item in list

# Some list functions
print(min(my_nums)) # smallest number in the list
print(max(my_nums)) # greatest number in the list
print(sum(my_nums)) # sum of numbers in the list

# Some list methods
my_list.append("Hal") # add Hal
print(my_list)
print(my_list.count("Abe")) # how many "Abe"s are there in the list?
my_list.append("Abe") # add Abe
print(my_list.count("Abe")) # now there are 2 Abes
my_list.insert(2, "Deb") # insert Deb into index 2 in the list, the third position (IN PROGRAMMING YOU COUNT 0, 1, 2, 3...)
print(my_list)

my_list.sort() # sort alphabetically
print(my_list)
my_list.append("erv") # in the ascii chart, all uppercase letters come before lowercase numbers
print(my_list)
my_list.sort()
print(my_list)

my_list.reverse() # reverses the order of the list
print(my_list)

# Important ones
my_list.pop() # takes off the last item in your list
print(my_list)

my_list.pop(0) # takes off the item at index 0 in your list
print(my_list)

#deleting items
del my_list[4]
print(my_list)

# find the index
print(my_list.index("Dan")) # will only return the first one. if there were two Dans, it wouldn't show you the second Dan

# ITERATION
my_list = []

for i in range(10):
    my_list.append(i)

print (my_list)

for num in my_list:
    num += 1 # num is just a copp, does not change the list
    print(num)
print(my_list)

# add 10 to each item (using index variable loop) (aka "for each" loop)
for i in range(len(my_list)):
    my_list[i] += 10
print (my_list)

# make a 2d list that is 10 x 10 [[0,0], [0,1], [0,2],...[9,9]]
my_list = []
for i in range (10):
    for j in range (10):
        my_list.append([i, j])
print (my_list)


# print each pair in the list
for pair in my_list:
    print(pair[0], pair[1])
    print(pair)

# add 10 to each item
for i in range(len(my_list)):
    for j in range(len(my_list[i])): # for i in range of the length of each sublist (2)
        my_list[i][j] += 10 # goes through to each sublist (i) and then adds 10 to each point of each sublist (j)

print (my_list)

# LIST COMPREHENSION
# Syntactic Sugar
# [returned_item for iterator in range/list filter]

# make a list from 0 to 100
my_list = [x for x in range(100)]
print(my_list)

# make a list of squares from 0 to 100
my_list = [x ** 2 for x in range(101)]
print(my_list)

# make a list of squares form 0 to 100, but only odd ones
my_list = [x ** 2 for x in range(100) if x ** 2 % 2 == 1] # MODULO
print(my_list)

#make a list of 100 random numbers from 1 to 100
my_list = [random.randrange(1, 101) for x in range(100)]
print(my_list)

# we can also go back through list to make a NEW list
my_list2 = [x for x in my_list]
print(my_list2)

for item in my_list:
    print(my_list)

# roll two dice 100 times and put in list
my_list = [[random.randrange(1,7), random.randrange(1,7)] for x in range(100)]
print(my_list)

# roll two dice 100 times and only keep the 7s
my_list = [x for x in[[random.randrange(1,7), random.randrange(1,7)] for x in range(100)]if x[0] + x[1] == 7]
print(my_list)

values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["H", "D", "C", "S"]

deck = []

for value in values:
    for suit in suits:
        deck.append(value + suit) # concatenation

print(deck)
print(values + suits)

# Strings using indices
first = "Aaron"
last = "Lee"
print (first + " " + last)
print (first[0])
print (first [-2:])
for char in first:
    print (char)
if "L" in last:
    print("Yep")

print(first.upper())

print('''
You
    can
        print
    like
this
    wow
        wow
    wowee
cool!
''')

print("Hello", end="HI")
print("World")