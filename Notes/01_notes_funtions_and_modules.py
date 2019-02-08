#January 29, 2019
import random
from math import pi as my_pi # import a single object and name it
from random import randrange as rand # import individual variables and name them as you please
from math import * # wildcard to import everything
from imports import my_import


def say_hi(name= "Mr. Lee"):
    '''

    :param name:
    :return:
    '''
    print("Hello", name)


def cube(n):
    return n ** 3

if __name__ == "__main__":
    '''
    this code runs when I execute THIS file
    '''
    say_hi()
    my_cube = cube(3)
    print (my_cube)
    print(cube(random.randrange(1, 101, 10))) # int from 1 to 100, jumping up by 10's
    print(random.random()) # float from 0 to 1

    print(my_pi) # prints pi from the math library
    print (rand(1,7)) # rolls a die
    print (cos(2)) # cosine of 2
