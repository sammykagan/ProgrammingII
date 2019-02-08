def say_hi(name= "Mr. Lee"):
    '''

    :param name:
    :return:
    '''
    print("Hello", name)


def cube(n):
    return n ** 3

say_hi("Sammy") #this will run on import

if __name__ == "__main__":
    #this will not run on import
    print(cube(5))
    say_hi("me")