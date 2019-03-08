# Friday, March 8
# Day before Dubai

# Sorting
import random
import time

# Swap values
a = 1
b = 2
print(a, b)

temp = a # store it before we destroy
a = b
b = temp
print(a, b)

# the pythonic way
a, b = b, a
print(a, b)

# make a random list of 100 numbers with value 1 to 99
# use list comprehension

# https://www.toptal.com/developers/sorting-algorithms (has algorithms, code, et. al.)

# WATCH THIS VIDEO https://www.youtube.com/channel/UCIqiLefbVHsOAXDAxQJH7Xw

randlist = [random.randrange(1, 100) for x in range(100)]
print(randlist)

def selection_sort(my_list):
    for current_position in range(len(my_list)):
        minimum_position = current_position
        for scan_position in range(current_position + 1, len(my_list)):
            if my_list[scan_position] < my_list[minimum_position]:
                minimum_position = scan_position
        my_list[current_position], my_list[minimum_position] = my_list[minimum_position], my_list[current_position]


start = time.time()
selection_sort(randlist)
end = time.time() - start
sample_range = 100
random_range = 100
print(randlist)
print("\nThat sort took", round(end,6), "seconds.\n")

# Insertion Sort
randlist = [random.randrange(1,random_range) for x in range(sample_range)]
print(randlist)

start = time.time()
for key_pos in range(1, len(randlist)):
    key_val = randlist[key_pos]
    scan_pos = key_pos - 1 # look to dancer on the left
    while (scan_pos >= 0) and (randlist[scan_pos] > key_val):
        randlist[scan_pos + 1] = randlist[scan_pos]
        scan_pos -= 1

    randlist[scan_pos + 1] = key_val

end = time.time() - start

print(randlist)

print("\nThat sort took", round(end,6), "seconds.")