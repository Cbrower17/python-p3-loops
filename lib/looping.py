#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10):
        print(f"{10-i}")
    print("Happy New Year!")
    pass
happy_new_year()
def square_integers(int_list):
    # code goes here!
    squared_list = [this_int*this_int for this_int in int_list]
    return squared_list
    pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

