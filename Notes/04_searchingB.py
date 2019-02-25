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
    villain_list = [x.strip() for x in Samé]

print(villain_list)
