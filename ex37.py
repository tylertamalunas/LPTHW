# and 
# logical operator that you use to make sure both statements are true or false
True and False
True and True

# as 
# used to rename an already existing item such as an import
# also used to make an alias
from random import randint as random_integer
print(random_integer(0,66))

# assert
# helps detect problems in code early when the cause is clear rather than later as a side effect.
# prints a custom message when there is an error
# use python -O to ignore these
# used as internal self checks
# helps locate exactly where an error is in the code.
assert True, "Errr"

print("that was weird")

# break
# stops a loop immediately
while True:
    print("Hi")
    break

# class
# defines a class 
# template for creating objects
# useless by itself, needs attributes associated with it
# can call specific modules in the class
class Snake:
    slither = "Sssssssss"
    hiss = "back off"
print(Snake.slither)
print(Snake.hiss)

# continue
# skip the iteration of a variable
# used to end the current iteration in a for or while loop and continue on
for i in range(9):
    if i == 3:
        continue
    print(i)

# def
# defines a funtion
def this_funtion():
    print("func")
this_funtion()

# del
# delete objects
# can be used on variables, lists, or parts of a list and more
class MyClass:
    name = "tyler"
del MyClass

# elif and else
# used after an if statement to try the next thing
# else is used to print something if the ifs and elifs dont work
x = 2
if x == 1:
    print("1")
elif x == 2:
    print("2")
else:
    print("3")

# except
# if exception happens do x
# used for exception handling
# try
# tries a certaion code block and if an exception happens, it shows the exception 
# without try, program will crash
# finally
# optional, is executed no matter what
# usually used to close objects and clean up resources, such as when opening files
try:
    print(y)
except:
    print("An exception occured")
finally:
    print("Well thats done")

# exec
# runs a string as python
z = 'name = "Ty"\nprint(name)'
exec(z)

# for
# loops over a collection of things
a = [1, "banana", 3]
for x in a:
    print(x)

# from
# import specific parts of a module
from sys import exit

# global
# declare that you want to use a global variable that has already been established
b = 2
def func1():
    global b
    b += 2
func1()
print(b)

# import
# imports a module to use in the code
import math

# in
# part of a for loop
# also tests if x in y
#word = salsa
#for x in y: 
 #   do thi

# is
# similar to ==
1 is 1
2 is 1

# lambda
# create a short anonymous function
s = lambda v: v + 10
print(s(5))