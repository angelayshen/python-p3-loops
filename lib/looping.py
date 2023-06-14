#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    number = 10
    while number > 0:
        print(number)
        number -= 1
    print('Happy New Year!')

def square_integers(int_list):
    # code goes here!
    return [i*i for i in int_list]

def fizzbuzz():
    # code goes here!
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)
