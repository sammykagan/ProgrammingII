# Formatting

import random

for i in range (10):
    x = random.randrange(1,101)
    y = random.randrange(1,101)
    z = round(x/y, 2) # round (number, digits)
    print(z)

a = 3.291238
print("My number is: {:.3f}".format(a)) # trim to three digits

b = 319048230958
print("b is: {:15}".format(b))

for i in range(20):
    c = random.randrange(10000)
    print("{:5}".format(c)) # justify right/trim to five decimals

# other stuff it can do
# :spacehold+justification+sign+width+commas?+precision+datatype+notation

for i in range(20):
    c = random.randrange(100000)
    print("{:>10}".format(c)) #justify left is <, center is ^, right is >

for i in range(20):
    c = random.randrange(-100000, 100000)
    print("{:+}".format(c)) # sign (+, -)

for i in range(20):
    c = random.randrange(-100000, 100000)
    print("{:,}".format(c)) # commas or not

for i in range(20):
    c = random.random() # random float from 0 to 1
    print("{:11.2f}".format(c)) # precision to 2 decimal

for i in range(20):
    c = random.random() # random float from 0 to 1
    print("{:11f}".format(c)) # represent as (f (float), d (int), b (binary)

for i in range(20):
    c = random.random()  # random float from 0 to 1
    print("{:10%}".format(c))  # (% or e)

for i in range(20):
    c = random.randrange(-1000, 1000)  * random.random()
    print("${:>8.2f}".format(c)) # right justified, total width of number is 8 spaces, float rounded to 2 decimals

for i in range(20):
    x = random.random() # random float 0 to 1
    y = random.randrange(1000) # random integer
    print()
    print("y is: {1:3} \nx is: {0:}\ny is: {1:2}".format(x, y)) # index to the left of colon -- in the
    # .format (x,y) x is in position 0 and y is in position 1 so putting the 0 and 1 before the {0:} allows us to
    #display things properly with the x following the "x is" and vice versa
