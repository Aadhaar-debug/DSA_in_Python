'''
A try block is the way to catch and recover from errors while a program
is running. If you have some code that may cause an error, but you dont
want it to crash your program, you can put the code in a try block. Then,
you can catch the error (also known as an exception) and deal with it. A
simple example might be a case where you want to convert some number
to a float. Many types of objects can be converted to float, but many
cannot. If we simply try to do the conversion and it works, everything is
ne. Otherwise, if there is a ValueError, we can do something else instead.
'''

x = "not a number"
try:
    f = float(x)
except ValueError:
    print("You crazy or somethin'")