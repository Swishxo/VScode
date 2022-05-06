#if example
a = 33
b = 200

#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
if b > a:
    print("b is greater")

#elif keyword, similar to else if in java
c = 2
d = 5
if c > d:
    print("C is greater")
elif c < d:
    print("C is less than D")
    #Can add as many elif you want

#The else keyword catches anything which isn't caught by the preceding conditions
if a == b:
    print("a and b are equal")
elif a > b:
    print("a is greater")
else:
    print("b is greater")

#You can also have an else without the elif
if a > b:
    print("a is greater")
else:
    print("b is greater")