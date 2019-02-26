# Searching (Chapter 15 on programarcadegames.com)

# select a file to read
file = open('data/villains.txt', 'r') # default is 'r'

for line in file:
    print(line.strip()) # strip removes leading and trailing spaces, new lines (/n), and tabs (/t)

file.close() # make sure to close it

file = open('data/villains.txt', 'r') # default is 'r')

for line in file:
    print("Hello", line.strip())

file.close()

# open a file to append to it.
file = open('data/villains.txt', 'a') # a for append

file.write("\nLee the Merciless")

file.close()

file = open('data/villains.txt', 'r')

for line in file:
    print("Hello", line.strip())

# open and write to a file (THIS OVERWRITES YOUR FILE)

file = open('data/oscars.txt', 'w') # if it doesn't exist, it creates one

file.write("Best Picture - Green Book\n")
file.write("Makeup and Hairstyling - Vice\n")

#easier way to open a file a read it
with open('data/villains.txt', 'r') as f:
    # we opened villains to read and assigned it to a name f
    for line in f:
        print(line.strip(), end="!\n")

# To use the data, read it into a list
with open('data/villains.txt') as Samé:
    villain_list = [x.strip().upper() for x in Samé]

print(villain_list)

# Linear Search
key = "LEE THE MERCILESS" # what we are looking for
i = 0 # the index of the loop

while i < len(villain_list) and key != villain_list[i]:
    i += 1 # loop will stop when it finds "THE DEADLY RAVEN"

if i < len(villain_list):
    print("Found", key, "at position", i)
else:
    print("Could not find", key)

# Binary Search  --- LINDSAY he basically just played a game with us to demonstrate this point: https://www.geeksforgeeks.org/binary-search/
villain_list.sort()
print(villain_list)
key = "RENARD THE TORTURER" #"Save big money at Renard's" -Nicky Lerner
# Mr. Lee laughed
# I laughed LOUDER


lower_bound = 0
upper_bound = len(villain_list) - 1
found = False
loops = 0 # counts the number of tries it too to find things
# with 2^7 loops, you can search 2^7 items in just 7 tries


# loop until we find it
while lower_bound <= upper_bound and not found:
    loops += 1
    middle_pos = (upper_bound + lower_bound) // 2
    if villain_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif villain_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True
if found:
    print("\nFound", key, "at position", middle_pos, "with", loops, "loops")
else:
    print("Could not find", key, "after", loops, "loops")

# go here now: http://programarcadegames.com/index.php?chapter=lab_spell_check
# this project is due at some random nebulous point in the future like all of our assignments

